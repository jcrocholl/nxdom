#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

import time
from datetime import datetime
import urllib2
import random

import adns
import ADNS

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub

from dns.models import TOP_LEVEL_DOMAINS, Lookup
from dns.utils import ip_to_int, int_to_ip
from domains.models import MAX_NAME_LENGTH, Domain
from domains.utils import random_domains
from utils.retry import retry, retry_objects

NAMESERVERS = """
208.67.222.222
208.67.220.220
156.154.70.1
156.154.71.1
4.2.2.1
4.2.2.2
4.2.2.3
4.2.2.4
4.2.2.5
4.2.2.6
209.244.0.3
209.244.0.4
216.87.84.211
141.211.125.17
141.211.144.17
205.171.2.65
205.171.3.65
""".split()

KNOWN_HIJACKERS = set("""
208.67.216.132
92.242.140.13
63.123.155.104
""".split())


def auth_func():
    return open('.passwd').read().split(':')


class NameServer(ADNS.QueryEngine):

    def __init__(self, ip):
        ADNS.QueryEngine.__init__(self, s=adns.init(
                adns.iflags.noautosys, sys.stderr, 'nameserver %s' % ip))
        self.ip = ip
        self.queries = 0
        self.results = {}

    def submit(self, name):
        self.queries += 1
        ADNS.QueryEngine.submit(self, name, adns.rr.A, 0,
                                self.callback, self.results)

    def callback(self, answer, name, rr, flags, results):
        # print name, answer
        ip_list = list(answer[3])
        if not ip_list:
            return
        ip_list.sort()
        ip = ip_list[0]
        if ip in KNOWN_HIJACKERS:
            return
        results[name] = ip

    def remove_hijacker(self):
        print "Server %-16s" % self.ip,
        if not self.results:
            print self.queries, "queries"
            return
        counters = {}
        for name in self.results:
            ip = self.results[name]
            counters[ip] = counters.get(ip, 0) + 1
        pairs = [(counters[ip], ip) for ip in counters]
        pairs.sort(reverse=True)
        if pairs[0][0] < self.queries - len(self.results):
            print self.queries, "queries,", len(self.results), "results"
            return # No DNS hijacker found.
        hijacker = pairs[0][1]
        print self.queries, "queries,",
        valid_results = len(self.results) - pairs[0][0]
        if valid_results:
            print valid_results, "results,",
        print pairs[0][0], "hijacked by %s" % hijacker
        for name in self.results.keys():
            if self.results[name] == hijacker:
                del self.results[name]


def update_dns(lookups, subdomain=None):
    if subdomain is None:
        print "Sending requests to name servers (without subdomain)..."
        prefix = ''
    else:
        print "Sending requests to name servers (subdomain %s)..." % subdomain
        prefix = subdomain + '.'
    servers = [NameServer(ip) for ip in NAMESERVERS]
    for lookup in lookups:
        for tld in TOP_LEVEL_DOMAINS:
            old_ip = getattr(lookup, tld)
            if old_ip == -1 or not old_ip:
                server = random.choice(servers)
                domain_name = prefix + lookup.key().name() + '.' + tld
                server.submit(domain_name)
    print "Waiting for DNS results..."
    results = {}
    start = time.time()
    finished = False
    while not finished:
        finished = True
        for server in servers:
            if not server.finished():
                server.run(0.1)
                if time.time() - start < 10 and not server.finished():
                    finished = False # Keep trying for max 10 seconds.
                else:
                    print "%-4.1fsec " % (time.time() - start),
                    server.remove_hijacker()
                    results.update(server.results)
    for lookup in lookups:
        display = False
        name = lookup.key().name()
        for tld in TOP_LEVEL_DOMAINS:
            domain_name = prefix + lookup.key().name() + '.' + tld
            if domain_name in results:
                setattr(lookup, tld, ip_to_int(results.get(domain_name)))
                display = True
            elif getattr(lookup, tld, None) is None:
                setattr(lookup, tld, 0)
        if display:
            print '%-16s' % name,
            for tld in TOP_LEVEL_DOMAINS:
                print '%-16s' % int_to_ip(getattr(lookup, tld)),
            print lookup.timestamp.strftime('%Y-%m-%d %H:%M')
        lookup.timestamp = datetime.now()


def main():
    for line in file('/etc/resolv.conf'):
        if line.startswith('nameserver'):
            nameserver, ip = line.strip().split()
            if ip not in NAMESERVERS:
                NAMESERVERS.append(ip)
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    parser.add_option('--batch', metavar='<size>', type="int", default=100,
                      help="adjust batch size (default 100)")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    if not args:
        while True:
            print "Trying to fetch %d oldest DNS lookups" % options.batch
            query = Lookup.all().order('timestamp')
            lookups = retry(query.fetch, options.batch)
            update_dns(lookups, 'www')
            update_dns(lookups)
            retry_objects(db.put, lookups)
    else:
        for filename in args:
            names = [line.strip() for name in open(filename)]
            print "Loaded %d names from %s" % (len(names), filename)
            lookup_names(names)


if __name__ == '__main__':
    main()
