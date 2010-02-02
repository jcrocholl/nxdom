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
from tools.retry import retry, retry_objects
from prefixes.selectors import random_prefix

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
141.211.125.17
141.211.144.17
205.171.2.65
205.171.3.65
""".split()


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
            error_string = status_name(status)
            if error_string == 'norecurse':
                sys.exit(11)
            results[name] = 'status=' + error_string


def update_dns(lookups, options):
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
                if (time.time() - start < options.timeout
                    and not server.finished()):
                    finished = False # Keep trying for timeout seconds.
                else:
                    print "%-4.1fsec " % (time.time() - start),
                    print "Server %-16s" % server.ip,
                    print "returned", len(server.results),
                    print "of", server.queries, "queries"
                    if (server.queries > 10 and
                        len(server.results) < server.queries / 2):
                        sys.exit(int(server.ip.split('.')[2]))
                    results.update(server.results)
    for lookup in lookups:
        display = False
        name = lookup.key().name()
        for tld in TOP_LEVEL_DOMAINS:
            domain_name = name + '.' + tld
            result = results.get(domain_name, 'timeout=%d' % options.timeout)
            if result != 'status=nxdomain':
                setattr(lookup, tld, reverse_name(result))
                display = True
        if display or options.verbose:
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
        print "timeout=%d for %d domains:" % (options.timeout, len(timeouts)),
        print ' '.join(timeouts)


def lookup_names(names, options):
    timestamp = datetime.now()
    lookups = [Lookup(key_name=name,
                      backwards=name[::-1],
                      timestamp=timestamp) for name in names]
    update_dns(lookups, options)
    return lookups


def update_oldest_lookups(options):
    print "Trying to fetch %d oldest names" % options.batch
    query = Lookup.all(keys_only=True).order('timestamp')
    keys = retry(query.fetch, options.batch)
    lookups = lookup_names([key.name() for key in keys], options)
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
    lookups = lookup_names([key.name() for key in keys], options)
    retry_objects(db.put, lookups)


def update_random(options):
    position = random.choice(('left', 'right'))
    keyword = random_prefix(position, length_choices=[2, 3, 4])
    for length in range(max(options.min, len(keyword) + 1),
                        options.max + 1):
        update_best_names(position, keyword, length, options)


def update_timeout(options):
    prefix = random_prefix('left', length_choices=[2, 3, 4])
    start_key = db.Key.from_path('dns_lookup', prefix)
    query = Lookup.all(keys_only=True).filter('com', 'timeout=20')
    query.filter('__key__ >', start_key)
    print "Trying to fetch %d names after %s with timeout=20" % (
        options.batch, prefix)
    keys = retry(query.fetch, options.batch)
    names = [key.name() for key in keys]
    lookups = lookup_names(names, options)
    retry_objects(db.put, lookups)


def upload_names(names, options):
    timestamp = datetime.now()
    domains = []
    for name in names:
        domain = Domain(key_name=name)
        domain.before_put()
        domains.append(domain)
    lookups = lookup_names(names, options)
    retry_objects(db.put, domains)
    retry_objects(db.put, lookups)


def count_existing(names):
    lookups = retry(Lookup.get_by_key_name, names)
    return sum([1 for lookup in lookups if lookup])


def bisect(names):
    # Check the end of the list.
    if count_existing(names[-10:]) > 5:
        return []
    # Check the beginning of the list.
    if count_existing(names[:10]) <= 5:
        return names
    # Bisect the list to find the crash point.
    left = 0
    right = len(names) - 1
    while right - left > 10:
        middle = (left + right) / 2
        count = count_existing(names[middle:middle+10])
        print "bisect left=%s right=%s middle=%s count=%d" % (
            names[left], names[right], names[middle], count)
        if count <= 5:
            right = middle
        else:
            left = middle
    return names[left:]


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
            if len(name) < options.min or len(name) > options.max:
                continue
            if name < options.resume:
                continue
            names.append(name)
        names.sort()
        print "Loaded %d names from %s" % (len(names), filename)
        if not options.resume:
            all_names = names
            names = bisect(all_names)
            print "Found %d of %d names already in the datastore." % (
                len(all_names) - len(names), len(all_names))
        while names:
            upload_names(names[:options.batch], options)
            names = names[options.batch:]
        options.resume = None


def main():
    for line in file('/etc/resolv.conf'):
        if line.startswith('nameserver'):
            nameserver, ip = line.strip().split()
            if ip not in NAMESERVERS:
                NAMESERVERS.append(ip)
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-v', '--verbose', action='store_true',
                      help="output all names, not only existing")
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    parser.add_option('--batch', metavar='<size>', type="int", default=60,
                      help="adjust batch size (default 60)")
    parser.add_option('--timeout', metavar='<seconds>', type="int", default=20,
                      help="maximum wait time for DNS response (default 20)")
    parser.add_option('--min', metavar='<length>', type="int", default=3,
                      help="only names of this length or longer (default 3)")
    parser.add_option('--max', metavar='<length>', type="int", default=9,
                      help="only names of this length or shorter (default 9)")
    parser.add_option('--left', metavar='<keyword>', default=None,
                      help="only names with this prefix")
    parser.add_option('--right', metavar='<keyword>', default=None,
                      help="only names with this suffix")
    parser.add_option('--random', action='store_true',
                      help="update random popular prefixes and suffixes")
    parser.add_option('--retry', action='store_true',
                      help="update lookups that had a timeout earlier")
    parser.add_option('--resume', metavar='<name>',
                      help="continue file upload from this name")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api_hidden', auth_func, options.server)
    if args:
        upload_files(args, options)
    elif options.random:
        while True:
            update_random(options)
    elif options.retry:
        while True:
            update_timeout(options)
    elif options.left is not None:
        for length in range(max(options.min, len(options.left)),
                            options.max + 1):
            update_best_names('left', options.left, length, options)
    elif options.right is not None:
        for length in range(max(options.min, len(options.right)),
                            options.max + 1):
            update_best_names('right', options.right, length, options)
    else:
        while True:
            update_oldest_lookups(options)


if __name__ == '__main__':
    main()
