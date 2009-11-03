#!/usr/bin/env python

import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])

from dictionaries import english

short = [word for word in english.SCOWL10 if len(word) <= 5]
short.sort()
for word1 in short:
    print word1
    for word2 in short:
        combo = word1 + word2
        if len(combo) <= 9:
            print combo
