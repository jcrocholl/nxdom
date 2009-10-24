#!/usr/bin/env python

import sys
import random

lines = []
if len(sys.argv) > 1:
    for filename in sys.argv[1:]:
        lines.extend(open(filename).readlines())
else:
    lines.extend(sys.stdin.readlines())
random.shuffle(lines)
for line in lines:
    print line.rstrip()
