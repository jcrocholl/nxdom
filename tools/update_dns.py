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
from dns.utils import ip_to_int, int_to_ip
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


def long_hash(text):
    """
    Hash to long integer with 60 bits to fit 64 bit datastore field
    without overflow.
    """
    return int(md5(text).hexdigest()[:15], 16)


def already_uploaded(names):
    random.shuffle(names)
    hundred = names[:100]
    domains = Domain.get_by_key_name(hundred)
    found = [domain.key().name() for domain in domains if domain is not None]
    if len(found) > len(hundred) / 2:
        print len(found), 'of these names are already in the datastore:'
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
        server_list = list(answer[3])
        if not server_list:
            return
        server_list.sort()
        results[name] = server_list[0][0]


def update_dns(lookups):
    servers = [NameServer(ip) for ip in NAMESERVERS]
    for lookup in lookups:
        for tld in TOP_LEVEL_DOMAINS:
            old_ip = getattr(lookup, tld)
            if old_ip == -1 or not old_ip:
                server = random.choice(servers)
                domain_name = lookup.key().name() + '.' + tld
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
                    print "Server %-16s" % server.ip,
                    print server.queries, "queries",
                    if server.results:
                        print "and", len(server.results), "results",
                    print
                    results.update(server.results)
    for lookup in lookups:
        display = False
        name = lookup.key().name()
        for tld in TOP_LEVEL_DOMAINS:
            domain_name = lookup.key().name() + '.' + tld
            if domain_name in results:
                # Set negative hash to distinguish from older IP values.
                setattr(lookup, tld, -long_hash(results.get(domain_name)))
                display = True
            elif getattr(lookup, tld, None) is None:
                setattr(lookup, tld, 0)
        if display:
            print '%-16s' % name,
            for tld in TOP_LEVEL_DOMAINS:
                print '%-16s' % results.get(name + '.' + tld, '')[:16],
            print lookup.timestamp.strftime('%Y-%m-%d %H:%M')
        lookup.timestamp = datetime.now()


def update_oldest_lookups(batch=100):
    print "Trying to fetch %d oldest DNS lookups" % batch
    query = Lookup.all().order('timestamp')
    lookups = retry(query.fetch, batch)
    update_dns(lookups)
    retry_objects(db.put, lookups)


def upload_names(names):
    domains = []
    lookups = []
    timestamp = datetime.now()
    for name in names:
        domain = Domain(key_name=name)
        domain.before_put()
        domains.append(domain)
        lookup = Lookup(key_name=name, backwards=name[::-1],
                        timestamp=timestamp)
        lookups.append(lookup)
    update_dns(lookups)
    retry_objects(db.put, domains)
    retry_objects(db.put, lookups)


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
        'scoretool', '/remote_api_hidden', auth_func, options.server)
    if not args:
        while True:
            update_oldest_lookups(options.batch)
    else:
        for filename in args:
            names = []
            for line in open(filename):
                name = line.strip()
                if ' ' in name and name[0] in '0123456789':
                    name = name.split()[-1]
                if '.' in name:
                    name = name.split('.')[0]
                if names and names[-1] == name:
                    continue
                if len(name) > 9:
                    continue
                names.append(name)
            print "Loaded %d names from %s" % (len(names), filename)
            if already_uploaded(names):
                return 1
            while names:
                upload_names(names[:options.batch])
                names = names[options.batch:]


if __name__ == '__main__':
    main()
