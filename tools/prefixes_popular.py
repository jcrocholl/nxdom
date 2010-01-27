#!/usr/bin/env python

import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

from prefixes.models import Prefix, Suffix

LENGTHS = range(2, 7)


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


def sort_prefixes(filename):
    counters = {}
    for line in open(filename):
        parts = line.strip().split()
        if len(parts) == 2:
            counters[parts[1]] = int(parts[0])
    names = counters.keys()
    names.sort(key=lambda name: -counters[name])
    return names


def all_lengths(Model, lengths):
    lower = Model.kind().split('_')[-1]
    upper = lower.upper()
    print 'POPULAR_' + upper + 'ES = {}'
    print upper + '_SCORES = {}'
    for length in lengths:
        print
        names = sort_prefixes('.data/popular/%ses.%d.txt' % (
                Model.kind().split('_')[-1], length))
        print 'POPULAR_%sES[%d] = """' % (upper, length)
        for name in names:
            print name
        print '""".split()'
        max_score = float(length) / max(lengths)
        print 'for index, name in enumerate(POPULAR_%sES[%d]):' % (
            upper, length)
        print '    %s_SCORES[name] = (%d - index) / %.1f' % (
            upper, len(names), len(names) / max_score)


def score_function(variable, slice):
    func = """
def prefix_score(name):
    best_score = 0.0
    best_prefix = ''
    for length in range(2, min(6, len(name)) + 1):
        prefix = name[slice]
        score = PREFIX_SCORES.get(prefix, None)
        if score > best_score:
            best_score = score
            best_prefix = prefix
    return best_score, best_prefix
""".strip()
    func = func.replace('PREFIX', variable)
    func = func.replace('prefix', variable.lower())
    func = func.replace('[slice]', slice)
    print '\n\n' + func


def main():
    all_lengths(Prefix, LENGTHS)
    print
    all_lengths(Suffix, LENGTHS)
    score_function('PREFIX', '[:length]')
    score_function('SUFFIX', '[-length:]')


if __name__ == '__main__':
    main()
