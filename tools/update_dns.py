#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

import time
from datetime import datetime
import random

import ADNS
from adns import rr

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from domains.models import MAX_NAME_LENGTH, DOMAIN_CHARS, TOP_LEVEL_DOMAINS
from domains.models import Domain, DnsLookup

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
        lookup = DnsLookup(key_name=name, timestamp = datetime.now())
        print '%-16s' % name,
        for tld in TOP_LEVEL_DOMAINS:
            ip = results.get('%s.%s' % (name, tld), '')
            setattr(lookup, tld, bool(ip))
            print '%-22s' % ('%s:%s' % (getattr(lookup, tld), ip)),
        print lookup.timestamp.strftime('%Y-%m-%d %H:%M')
        lookups.append(lookup)
    retry(db.put, lookups)


def fetch_server_names():
    query = Domain.all(keys_only=True)
    length = random.choice(range(4))
    if not length:
        name = ''.join([random.choice(DOMAIN_CHARS) for i in range(10)])
        random_key = db.Key.from_path('domains_domain', name)
        print "Fetching names greater than", name
        query.filter('__key__ >', random_key)
    else:
        name = ''.join([random.choice(DOMAIN_CHARS) for i in range(length)])
        print "Fetching the shortest names that start with", name
        query.filter('left%d' % len(name), name).order('length')
    keys = query.fetch(BATCH_SIZE)
    names = [key.name() for key in keys if len(key.name()) < MAX_NAME_LENGTH]
    if names:
        return names
    else: # Try again.
        return fetch_server_names()


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
            lookup_names(fetch_server_names())
    else:
        for filename in args:
            lookup_names([line.strip() for name in open(filename)])


if __name__ == '__main__':
    main()
