#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])

from languages.utils import word_score
from languages import english, spanish, french, german

WORDS = """
ich mit einem wenig kostenlosen begabten verschraubenden
Fuchs Traum Menschenfresser Dampfschiffahrt Dampfschifffahrt
me with another little inexpensive ridiculous interlocking
Python beautiful illusionist Antidisestablishmentarianism
""".split()


print '%-8s %-8s %-8s %-8s %s' % tuple('english spanish french german word'.split())

for word in WORDS:
    print '%-8d %-8d %-8d %-8d %s' % (
        word_score(word, english.TRIPLE_SCORES),
        word_score(word, spanish.TRIPLE_SCORES),
        word_score(word, french.TRIPLE_SCORES),
        word_score(word, german.TRIPLE_SCORES),
        word,
)
