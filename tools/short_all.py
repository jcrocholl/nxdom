#!/usr/bin/env python

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

for c1 in LETTERS:
    for c2 in LETTERS:
        for c3 in LETTERS:
            for c4 in LETTERS:
                print ''.join((c1, c2, c3, c4))
