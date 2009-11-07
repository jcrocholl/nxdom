#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])

import textwrap

from dictionaries import english
from readability.utils import word_triples


def count_triples(words, counters):
    for word in words:
        for triple in word_triples(word):
            counters[triple] = counters.get(triple, 0) + 1


def print_score(triples, score):
    triples.sort()
    print
    print 'for triple in """'
    print textwrap.fill(' '.join(triples))
    print '""".split(): TRIPLE_SCORES[triple] =', score


if __name__ == '__main__':
    counters = {}
    count_triples(english.SCOWL10, counters)
    count_triples(english.SCOWL20, counters)
    count_triples(english.SCOWL35, counters)
    count_triples(english.SCOWL50, counters)
    pairs = [(counters[triple], triple) for triple in counters]
    pairs.sort()
    score = -1
    previous = 1
    triples = []
    utils = open('readability/utils.py').readlines()
    while utils[0].strip():
        print utils.pop(0).rstrip()
    for count, triple in pairs:
        if count != previous:
            if len(triples) >= 400:
                if score >= 1:
                    print_score(triples, score)
                triples = []
                score += 1
            previous = count
        triples.append(triple)
    if triples:
        print_score(triples, score)
    for line in utils:
        print line.rstrip()
