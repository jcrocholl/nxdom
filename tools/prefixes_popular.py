#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from prefixes.models import DotComPrefix, DotComSuffix


def auth_func():
    return open('.passwd').read().split(':')


def most_popular(query, variable):
    print 'for index, part in enumerate("""'
    query.order('-count')
    total = 0
    for prefix in query.fetch(1000):
        if prefix.count < 10:
            break
        print prefix.key().name()
        total += 1
    print '""".split()): %s[part] = (%d - index) / %d.0' % (
        variable, total, total)
    print


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    print 'PREFIX_SCORES = {}'
    for length in range(3, 7):
        most_popular(DotComPrefix.all().filter('length', length),
                     'PREFIX_SCORES')
    print 'SUFFIX_SCORES = {}'
    for length in range(3, 7):
        most_popular(DotComSuffix.all().filter('length', length),
                     'SUFFIX_SCORES')


if __name__ == '__main__':
    main()
