#!/usr/bin/env python

import sys
import time
import urllib2


def milliseconds(url):
    start = time.time()
    html = urllib2.urlopen(url).read()
    finish = time.time()
    return int(1000 * (finish - start))


def main():
    url = 'http://www.nxdom.com/'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    results = [milliseconds(url) for i in range(10)]
    results.sort()
    print time.strftime('%Y-%m-%d %H:%M:%S'),
    print ' '.join([str(i) for i in results])


if __name__ == '__main__':
    main()
