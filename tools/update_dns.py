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
from hashlib import md5

import adns
import ADNS

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub

from dns.models import TOP_LEVEL_DOMAINS, Lookup
from dns.utils import status_name, reverse_name
from domains.models import MAX_NAME_LENGTH, Domain
from domains.utils import random_domains
from utils.retry import retry, retry_objects

NAMESERVERS = """
208.67.222.222
208.67.220.220
8.8.8.8
8.8.4.4
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


def auth_func():
    return open('.passwd').read().split(':')


def already_uploaded(names):
    if len(names) < 10:
        return False
    sample = names[:]
    random.shuffle(sample)
    sample = sample[:100]
    domains = Domain.get_by_key_name(sample)
    found = [domain.key().name() for domain in domains if domain is not None]
    if len(found) > len(sample) / 2:
        print len(found) * 100 / len(sample),
        print 'percent of these names are already in the datastore:'
        print ' '.join(found)
        return True


class NameServer(ADNS.QueryEngine):

    def __init__(self, ip):
        ADNS.QueryEngine.__init__(self, s=adns.init(
                adns.iflags.noautosys, sys.stderr, 'nameserver %s' % ip))
        self.ip = ip
        self.queries = 0
        self.results = {}

    def submit(self, name):
        self.queries += 1
        ADNS.QueryEngine.submit(self, name, adns.rr.SOA, 0,
                                self.callback, self.results)

    def callback(self, answer, name, rr, flags, results):
        # print name, answer
        status = answer[0]
        server_list = list(answer[3])
        if server_list:
            server_list.sort()
            results[name] = server_list[0][0]
        else:
            results[name] = 'status=' + status_name(status)


def update_dns(lookups, timeout=20):
    servers = [NameServer(ip) for ip in NAMESERVERS]
    for lookup in lookups:
        name = lookup.key().name()
        for tld in TOP_LEVEL_DOMAINS:
            server = random.choice(servers)
            domain_name = name + '.' + tld
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
                if time.time() - start < timeout and not server.finished():
                    finished = False # Keep trying for timeout seconds.
                else:
                    print "%-4.1fsec " % (time.time() - start),
                    print "Server %-16s" % server.ip,
                    print "returned", len(server.results),
                    print "of", server.queries, "queries"
                    results.update(server.results)
    for lookup in lookups:
        display = False
        name = lookup.key().name()
        for tld in TOP_LEVEL_DOMAINS:
            domain_name = name + '.' + tld
            result = results.get(domain_name, 'timeout=%d' % timeout)
            if result != 'status=nxdomain':
                setattr(lookup, tld, reverse_name(result))
                display = True
        if display:
            print '%-12s' % name,
            for tld in TOP_LEVEL_DOMAINS:
                print tld if getattr(lookup, tld, None) else ' ' * len(tld),
            print
    timeouts = []
    for lookup in lookups:
        for tld in TOP_LEVEL_DOMAINS:
            if hasattr(lookup, tld):
                if getattr(lookup, tld).startswith('timeout='):
                    timeouts.append(lookup.key().name() + '.' + tld)
    if timeouts:
        print "timeout=%d for %d domains:" % (timeout, len(timeouts)),
        print ' '.join(timeouts)


def lookup_names(names, timeout):
    timestamp = datetime.now()
    lookups = [Lookup(key_name=name,
                      backwards=name[::-1],
                      timestamp=timestamp) for name in names]
    update_dns(lookups, timeout)
    return lookups


def update_oldest_lookups(options):
    print "Trying to fetch %d oldest names" % options.batch
    query = Lookup.all(keys_only=True).order('timestamp')
    keys = retry(query.fetch, options.batch)
    lookups = lookup_names([key.name() for key in keys], options.timeout)
    retry_objects(db.put, lookups)


def update_best_names(position, keyword, length, options):
    print "Trying to fetch %d best names with" % options.batch,
    if keyword and position == 'left':
        print "prefix", keyword, "and",
    if keyword and position == 'right':
        print "suffix", keyword, "and",
    print "length", length
    query = Domain.all(keys_only=True)
    if keyword:
        query.filter('%s%d' % (position, len(keyword)), keyword)
    query.filter('length', length)
    query.order('-score')
    keys = retry(query.fetch, options.batch)
    if not keys:
        return
    lookups = lookup_names([key.name() for key in keys], options.timeout)
    retry_objects(db.put, lookups)


def upload_names(names, options):
    timestamp = datetime.now()
    domains = []
    for name in names:
        domain = Domain(key_name=name)
        domain.before_put()
        domains.append(domain)
    lookups = lookup_names(names, options.timeout)
    retry_objects(db.put, domains)
    retry_objects(db.put, lookups)


def upload_files(filenames, options):
    for filename in filenames:
        names = []
        for line in open(filename):
            name = line.strip()
            if ' ' in name and name[0] in '0123456789':
                name = name.split()[-1]
            if '.' in name:
                name = name.split('.')[0]
            if options.left and not name.startswith(options.left):
                continue
            if options.right and not name.startswith(options.right):
                continue
            if names and names[-1] == name:
                continue
            if len(name) > options.max:
                continue
            names.append(name)
        print "Loaded %d names from %s" % (len(names), filename)
        if already_uploaded(names):
            continue
        while names:
            upload_names(names[:options.batch], options)
            names = names[options.batch:]


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
    parser.add_option('--timeout', metavar='<seconds>', type="int", default=20,
                      help="maximum wait time for DNS response (default 20)")
    parser.add_option('--max', metavar='<length>', type="int", default=9,
                      help="only names of this length or shorter (default 9)")
    parser.add_option('--left', metavar='<keyword>', default=None,
                      help="only names with this prefix")
    parser.add_option('--right', metavar='<keyword>', default=None,
                      help="only names with this suffix")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api_hidden', auth_func, options.server)
    if args:
        upload_files(args, options)
    elif options.left is not None:
        for length in range(max(3, len(options.left)), options.max + 1):
            update_best_names('left', options.left, length, options)
    elif options.right is not None:
        for length in range(max(3, len(options.right)), options.max + 1):
            update_best_names('right', options.right, length, options)
    else:
        while True:
            update_oldest_lookups(options)


if __name__ == '__main__':
    main()
