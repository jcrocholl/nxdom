#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

from languages import english
from languages.utils import word_score

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

for c1 in LETTERS:
    for c2 in LETTERS:
        for c3 in LETTERS:
            for c4 in LETTERS:
                for c5 in LETTERS:
                    word = ''.join((c1, c2, c3, c4, c5))
                    score = word_score(word, english.TRIPLE_SCORES)
                    if score > 0.5:
                        print '%.5f %s' % (score, word)
