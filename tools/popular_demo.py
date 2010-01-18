#! /usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from prefixes import popular

words = set([word.lower() for word in open('license.txt').read().split()])

prefixes = [(popular.prefix_score(word), word) for word in words]
prefixes.sort()
for pair, word in prefixes:
    score, part = pair
    print '%.5f %s %s' % (score, part, word)

suffixes = [(popular.suffix_score(word), word) for word in words]
suffixes.sort()
for pair, word in suffixes:
    score, part = pair
    print '%.5f %s %s' % (score, part, word)
