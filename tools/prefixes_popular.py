#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

from pprint import pprint

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from prefixes.models import DotComPrefix, DotComSuffix
from tools.retry import retry

LENGTHS = range(3, 10)


def auth_func():
    return open('.passwd').read().split(':')


def most_popular(model, variable, length, maximums, totals):
    query = model.all()
    query.filter('length', length),
    query.order('-count')
    total = maximum = 0
    counters = []
    prefixes = retry(query.fetch, 1000)
    for prefix in prefixes:
        if prefix.count < 10:
            break
        counters.append((prefix.key().name(), prefix.count))
        if prefix.count > maximum:
            maximum = prefix.count
        total += prefix.count
    counters.sort(key=lambda pair: -pair[1])
    print '%s[%d] = {' % (variable, length)
    for pair in counters:
        print "'%s': %d," % pair
    print '}'
    totals[length] = int(total)
    maximums[length] = int(maximum)


def all_lengths(model, variable, lengths):
    # Fetch and format popular prefixes.
    totals = {}
    maximums = {}
    print '%s_SCORES = {}' % variable
    for length in lengths:
        most_popular(model, '%s_SCORES' % variable,
                     length, maximums, totals)
    print '%s_MAXIMUMS = ' % variable,
    pprint(maximums)
    print '%s_TOTALS = ' % variable,
    pprint(totals)


def score_function(variable, slice):
    func = """

def prefix_score(name):
    best_score = 0.0
    best_prefix = ''
    for length in range(3, min(10, len(name) + 1)):
        prefix = name[slice]
        score = PREFIX_SCORES[length].get(prefix, 0)
        score /= float(PREFIX_MAXIMUMS[length])
        if score and score >= best_score:
            best_score = score
            best_prefix = prefix
    return best_score, best_prefix
"""
    func = func.replace('PREFIX', variable)
    func = func.replace('prefix', variable.lower())
    func = func.replace('[slice]', slice)
    print func.rstrip()


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api_hidden', auth_func, options.server)
    all_lengths(DotComPrefix, 'PREFIX', LENGTHS)
    print
    all_lengths(DotComSuffix, 'SUFFIX', LENGTHS)
    score_function('PREFIX', '[:length]')
    score_function('SUFFIX', '[-length:]')


if __name__ == '__main__':
    main()
