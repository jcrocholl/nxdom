#!/usr/bin/env python

import sys
import adns
import ADNS
from hashlib import md5

sys.path.append('.')
from dns.utils import status_name


def callback(answer, name, rr, flags, data):
    print name, data, status_name(answer[0])
    for entry in answer[3]:
        if data == 'SOA':
            print '   ', entry[0]
        else:
            print '   ', entry


engine = ADNS.QueryEngine()
for name in sys.argv[1:]:
    engine.submit(name, adns.rr.SOA, 0, callback, 'SOA')
    engine.submit(name, adns.rr.A, 0, callback, 'NS')
    engine.submit(name, adns.rr.A, 0, callback, 'A')
    while not engine.finished():
        engine.run(0.1)
