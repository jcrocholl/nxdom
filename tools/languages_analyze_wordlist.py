#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])

from languages.utils import word_triples

import re

ACCEPTABLE_WORD_REGEX = re.compile('^[a-z0-9-]+$')


def count_triples(words, counters):
    rejfile = open('rejected.txt', 'w')
    for word in words:
        word = word.lower().strip()
        word = word.lstrip('*').rstrip('#')
        word = word.replace('\\', '').replace('/', '')
        word = word.replace('~', '').replace('$', '')
        word = word.replace('^', '').replace('`', '')
        word = word.replace('"', '').replace("'", '')
        if not ACCEPTABLE_WORD_REGEX.match(word):
            print >> rejfile, word
            continue
        for triple in word_triples(word):
            counters[triple] = counters.get(triple, 0) + 1
    rejfile.close()


if __name__ == '__main__':
    counters = {}
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            count_triples(open(filename), counters)
    else:
        count_triples(sys.stdin, counters)
    pairs = [(counters[triple], triple) for triple in counters]
    pairs.sort(reverse=True)
    pairs = pairs[:20000]
    print 'TRIPLE_SCORES = {}'
    print 'for index, triple in enumerate("""'
    line = []
    for count, triple in pairs:
        line.append(triple)
        if len(' '.join(line)) > 78:
            print ' '.join(line[:-1])
            line = [triple]
    if line:
        print ' '.join(line)
    print '""".split()): TRIPLE_SCORES[triple] = (%d - index) * 100 / %d' % (
        len(pairs), len(pairs))
