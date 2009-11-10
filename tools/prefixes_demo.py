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
from prefixes.models import Prefix, Suffix, DotComPrefix, DotComSuffix


def auth_func():
    return open('.passwd').read().split(':')


def main():
    for name in 'ab as ax ur we'.split():
        prefix = Prefix(key_name=name, length=len(name))
        prefix.count_domains()
        print prefix
        suffix = Suffix(key_name=name, length=len(name))
        suffix.count_domains()
        print suffix
    for length in range(3, 7):
        prefix = DotComPrefix(key_name='urcollection'[:length], length=length)
        prefix.count_domains()
        print prefix
        suffix = DotComSuffix(key_name='urcollection'[-length:], length=length)
        suffix.count_domains()
        print suffix


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>', default=None,
                      help="connect to a remote server")
    parser.add_option('--resume', metavar='<name>',
                      help="resume upload, starting from this name")
    (options, args) = parser.parse_args()
    if options.server:
        remote_api_stub.ConfigureRemoteDatastore(
            'scoretool', '/remote_api', auth_func, options.server)
    main()
