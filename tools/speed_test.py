#!/usr/bin/env python

import sys
import time
import urllib2

NUM_REQUESTS = 20

etag = None
last_modified = None


def milliseconds(url):
    info = ''
    request = urllib2.Request(url)
    global etag, last_modified
    if etag:
        request.add_header('If-None-Match', etag)
    if last_modified:
        request.add_header('If-Modified-Since', last_modified)
    start = time.time()
    try:
        response = urllib2.urlopen(request)
        if 'Etag' in response.headers:
            etag = response.headers['etag']
        if 'Last-Modified' in response.headers:
            last_modified = response.headers['Last-Modified']
        html = response.read()
    except urllib2.HTTPError, status:
        if status.code == 304:
            info = '='
        else:
            raise
    finish = time.time()
    return (1000 * (finish - start), info)


def main():
    url = 'http://www.nxdom.com/'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    results = [milliseconds(url) for i in range(NUM_REQUESTS)]
    results.sort()
    print time.strftime('%Y-%m-%d %H:%M:%S'),
    print ' '.join(['%d%s' % pair for pair in results])


if __name__ == '__main__':
    main()
