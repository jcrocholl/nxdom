#! /usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

import logging
import random

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub

from dns.models import TOP_LEVEL_DOMAINS, Lookup
from domains.models import MAX_NAME_LENGTH, DOMAIN_CHARS, Domain
from tools.retry import retry, retry_objects

PASSWORD_FILENAME = '.passwd'
BATCH_SIZE = 100
PURGE_VALUES = """
status=rcodeservfail
status=prohibitedcname
status=nodata
timeout=30
""".split()

def auth_func():
    if os.path.exists(PASSWORD_FILENAME):
        return open(PASSWORD_FILENAME).read().split(':')
    username = raw_input('Username:')
    password = getpass.getpass('Password:')
    return username, password

logger = logging.getLogger("google.appengine.tools.appengine_rpc")
logger.setLevel(logging.INFO)

remote_api_stub.ConfigureRemoteDatastore(
    'scoretool', '/remote_api_hidden', auth_func, 'scoretool.appspot.com')

while PURGE_VALUES:
    query = Lookup.all(keys_only=True)
    value = random.choice(PURGE_VALUES)
    query.filter('com', value)
    keys = retry(query.fetch, BATCH_SIZE)
    if len(keys) < BATCH_SIZE:
        PURGE_VALUES.remove(value)
    if len(keys):
        print "deleting %d names (%s to %s) where com is %s" % (
            len(keys), keys[0].name(), keys[-1].name(), value)
        domain_keys = [db.Key.from_path('domains_domain', key.name())
                       for key in keys]
        db.delete(keys + domain_keys)
