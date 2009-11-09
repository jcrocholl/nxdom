#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])

from readability.utils import score_readability
from readability.english import TRIPLE_SCORES as english_scores
from readability.german import TRIPLE_SCORES as german_scores

WORDS = """
ich mit einem wenig kostenlosen begabten verschraubenden
Fuchs Traum Menschenfresser Dampfschiffahrt Dampfschifffahrt
me with another little inexpensive ridiculous interlocking
Python beautiful illusionist Antidisestablishmentarianism
""".split()

for word in WORDS:
    print '%-20s %5d %5d' % (
        word,
        score_readability(word, english_scores),
        score_readability(word, german_scores))
