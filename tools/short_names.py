#!/usr/bin/env python

import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])

from dictionaries import english

word_length = int(sys.argv[1])
short = [word for word in english.SCOWL10 if len(word) <= 5]
short.sort()
for word1 in short:
    if len(word1) == word_length:
        print word1
        continue
    for word2 in short:
        combo = word1 + word2
        if len(combo) == word_length:
            print combo
