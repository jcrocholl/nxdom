#!/usr/bin/env python

import unicodedata

SCOWL_FINAL_DIR = '../scowl-6/final'
MAX_LINE_LENGTH = 70

print """
# Copyright 2000-2004 by Kevin Atkinson
# Python wrapper by Johann C. Rocholl
#
# Permission to use, copy, modify, distribute and sell these word
# lists, the associated scripts, the output created from the scripts,
# and its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appears in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation. Kevin Atkinson makes no representations
# about the suitability of this array for any purpose. It is provided
# "as is" without express or implied warranty.
""".strip()

def pythonize_wordlist(constant, wordlist):
    print
    print constant, '= set("""'
    line = ''
    for word in wordlist:
        if len(line) + 1 + len(word) > MAX_LINE_LENGTH:
            print line
            line = ''
        if line:
          line += ' '
        line += word
    if line:
        print line
    print '""".split())'


def load_wordlist(number):
    wordlist = []
    filename = '%s/english-words.%d' % (SCOWL_FINAL_DIR, number)
    for word in open(filename):
        if "'" in word:
            continue
        latin1 = word.strip()
        word = latin1.decode('latin1')
        word = unicodedata.normalize('NFKD', word)
        ascii = word.encode('ASCII', 'ignore')
        wordlist.append(ascii)
    return wordlist


for number in (10, 20, 35, 50):
    wordlist = load_wordlist(number)
    if number == 50:
        wordlist += load_wordlist(40)
    wordlist.sort()
    pythonize_wordlist('SCOWL%d' % number, wordlist)
