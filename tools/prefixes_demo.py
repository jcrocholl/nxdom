#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

import datetime

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from domains.models import Domain
from prefixes.models import DotComPrefix


def auth_func():
    return open('.passwd').read().split(':')


def main():
    for length in range(3, 7):
        prefix = DotComPrefix(key_name='urcollection'[:length])
        prefix.count_domains()
        print prefix


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    parser.add_option('--resume', metavar='<name>',
                      help="resume upload, starting from this name")
    (options, args) = parser.parse_args()
    if options.server != 'dev':
        remote_api_stub.ConfigureRemoteDatastore(
            'scoretool', '/remote_api', auth_func, options.server)
    main()
