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

from domains.models import DOMAIN_CHARS
from prefixes.models import Prefix


def auth_func():
    return open('.passwd').read().split(':')


def print_counts(name, counts):
    print name, '= {'
    keys = counts.keys()
    keys.sort()
    for key in keys:
        if counts[key]:
            print "'%s': %d," % (key, counts[key])
    print '}'


def main():
    one = {}
    two = {}
    for c1 in DOMAIN_CHARS:
        query = Prefix.all().filter('length', 2)
        query.filter('__key__ >', db.Key.from_path('prefixes_prefix', c1))
        next = chr(ord(c1) + 1)
        query.filter('__key__ <', db.Key.from_path('prefixes_prefix', next))
        one[c1] = 0
        for prefix in query.fetch(100):
            one[c1] += prefix.count
            two[prefix.key().name()] = prefix.count
    print_counts('ONE', one)
    print_counts('TWO', two)


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    main()
