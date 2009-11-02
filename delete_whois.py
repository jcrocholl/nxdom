#!/usr/bin/env python

import os
import sys
import time
import getpass
import datetime

from common.appenginepatch.aecmd import setup_env
setup_env()

import ADNS
from adns import rr

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from domains.models import Domain, Whois

BATCH_SIZE = 400
MAX_ATTEMPTS = 5


def auth_func():
    return open('.passwd').read().split(':')


def delete_batch(objects):
    if not objects:
        return
    for attempt in range(MAX_ATTEMPTS):
        if attempt:
            print "Attempt %d of %d will start in %d seconds." % (
                attempt + 1, MAX_ATTEMPTS, attempt)
            time.sleep(attempt)
        print "Deleting %d objects (%s to %s):" % (
            len(objects), objects[0].name(), objects[-1].name())
        try:
            db.delete(objects)
            break
        except Timeout:
            print "*** Timeout ***"
            if attempt + 1 == MAX_ATTEMPTS:
                sys.exit(1)
    del objects[:]


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    while True:
        whois_keys = Whois.all(keys_only=True).fetch(BATCH_SIZE)
        delete_batch(whois_keys)


if __name__ == '__main__':
    main()
