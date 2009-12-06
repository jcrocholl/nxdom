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
    query.order('-count')
    total = 0
    counters = []
    for prefix in query.fetch(1000):
        if prefix.count < 10:
            break
        counters.append((prefix.key().name(), prefix.count))
        total += prefix.count
    print variable + '_TOTAL =', total
    counters.sort()
    print variable, '= ['
    for pair in counters:
        print "('%s', %d)," % pair
    print ']'
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
    for length in range(3, 11):
        most_popular(DotComPrefix.all().filter('length', length),
                     'LEFT%d' % length)
    print 'SUFFIX_SCORES = {}'
    for length in range(3, 11):
        most_popular(DotComSuffix.all().filter('length', length),
                     'RIGHT%d' % length)


if __name__ == '__main__':
    main()
