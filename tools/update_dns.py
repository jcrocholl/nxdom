#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

import time
from datetime import datetime

import ADNS
from adns import rr

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from dns.models import TOP_LEVEL_DOMAINS, Lookup
from domains.models import MAX_NAME_LENGTH, Domain
from domains.utils import get_random_names

BATCH_SIZE = 100
MAX_ATTEMPTS = 5


def auth_func():
    return open('.passwd').read().split(':')


def retry(func, objects):
    if not objects:
        return
    for attempt in range(MAX_ATTEMPTS):
        if attempt:
            print "Attempt %d of %d will start in %d seconds." % (
                attempt + 1, MAX_ATTEMPTS, attempt)
            time.sleep(attempt)
        print "Trying to %s %d objects (%s to %s):" % (
            func.__name__, len(objects),
            objects[0].key().name(), objects[-1].key().name())
        try:
            return func(objects)
        except Timeout:
            print "*** Timeout ***"
            if attempt + 1 >= MAX_ATTEMPTS:
                raise


def callback(answer, name, rr, flags, results):
    # print name, answer
    ip_list = list(answer[3])
    if not ip_list:
        return
    if name.startswith('www.'):
        name = name[4:]
    ip_list.sort()
    results[name] = ip_list[0]


def detect_dns_hijacker(results, threshold):
    counters = {}
    for name in results:
        ip = results[name]
        counters[ip] = counters.get(ip, 0) + 1
    if not counters:
        return
    pairs = [(counters[ip], ip) for ip in counters]
    pairs.sort(reverse=True)
    if pairs[0][0] < threshold:
        return # No DNS hijacker found.
    hijacker = pairs[0][1]
    print "DNS hijacker detected: %d of %d results returned %s." % (
        pairs[0][0], len(results), hijacker)
    for name in results:
        ip = results[name]
        if ip == hijacker:
            results[name] = None


def lookup_names(names):
    results = {}
    dns = ADNS.QueryEngine()
    for name in names:
        for tld in TOP_LEVEL_DOMAINS:
            dns.submit('%s.%s' % (name, tld), rr.A, 0, callback, results)
            dns.submit('www.%s.%s' % (name, tld), rr.A, 0, callback, results)
    print "Waiting for DNS results..."
    dns.finish()
    # Threshold is the number of NXDOMAIN results.
    threshold = len(names) * len(TOP_LEVEL_DOMAINS) - len(results)
    # Remove IP address if it has more results than NXDOMAIN did.
    detect_dns_hijacker(results, threshold)
    lookups = []
    for name in names:
        lookup = Lookup(key_name=name, backwards=name[::-1],
                        timestamp=datetime.now())
        print '%-16s' % name,
        for tld in TOP_LEVEL_DOMAINS:
            ip = results.get('%s.%s' % (name, tld), '')
            setattr(lookup, tld, bool(ip))
            print '%-16s' % ip,
        print lookup.timestamp.strftime('%Y-%m-%d %H:%M')
        lookups.append(lookup)
    retry(db.put, lookups)


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    if not args:
        while True:
            names, description = get_random_names(BATCH_SIZE)
            print "Fetched %d %s" % (len(names), description)
            print ' '.join(names)
            lookup_names(names)
    else:
        for filename in args:
            names = [line.strip() for name in open(filename)]
            print "Loaded %d names from %s" % (len(names), filename)
            lookup_names(names)


if __name__ == '__main__':
    main()
