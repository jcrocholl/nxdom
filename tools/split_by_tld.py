#!/usr/bin/env python

import sys
import os
import re


DATE_REGEX = re.compile(r'(\d+)-(\d+)-(\d+)')


def split(filename):
    month, day, year = DATE_REGEX.match(os.path.basename(filename)).groups()
    tld_names = {}
    for line in open(filename):
        domain = line.strip()
        if not '.' in domain:
            continue
        name, tld = domain.split('.')
        if tld not in tld_names:
            tld_names[tld] = []
        tld_names[tld].append(name)
    for tld in tld_names:
        outfilename = '%s-%s-%s.%s.txt' % (year, month, day, tld)
        outfile = open(outfilename, 'w')
        names = tld_names[tld]
        column = 0
        for name in names:
            if column:
                if column + 1 + len(name) > 78:
                    outfile.write('\n')
                    column = 0
                else:
                    outfile.write(' ')
                    column += 1
            outfile.write(name)
            column += len(name)
        outfile.close()


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        split(filename)
