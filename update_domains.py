#!/usr/bin/env python

import os
import sys
import time
import getpass
import datetime

from common.appenginepatch.aecmd import setup_env
setup_env()

import ADNS
from adns import rr

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from domains.models import Domain, Whois, Dns

BATCH_SIZE = 20
MAX_ATTEMPTS = 5
MAX_NAME_LENGTH = 16
DNS_HIJACKERS = '208.67.219.132'.split()


def auth_func():
    return open('.passwd').read().split(':')


def put(objects):
    if not objects:
        return
    for attempt in range(MAX_ATTEMPTS):
        if attempt:
            print "Attempt %d of %d will start in %d seconds." % (
                attempt + 1, MAX_ATTEMPTS, attempt)
            time.sleep(attempt)
        print "Uploading %d objects (%s to %s):" % (
            len(objects), objects[0].key().name(), objects[-1].key().name())
        try:
            db.put(objects)
            break
        except Timeout:
            print "*** Timeout ***"
            if attempt + 1 == MAX_ATTEMPTS:
                sys.exit(1)
    del objects[:]


def get_oldest_domains():
    result = []
    for domain in Domain.all().order('timestamp').fetch(BATCH_SIZE):
        if len(domain.key().name()) <= MAX_NAME_LENGTH:
            result.append(domain)
        else:
            domain.delete()
    return result


def callback(answer, qname, rr, flags, domain):
    print qname, answer
    ip_list = list(answer[3])
    ip_list.sort()
    ip = ip_list[0] if ip_list else None
    if ip in DNS_HIJACKERS:
        ip = None
    if ip:
        setattr(domain, qname[-3:], ip)


def update_domains():
    dns = ADNS.QueryEngine()
    domains = get_oldest_domains()
    for domain in domains:
        name = domain.key().name()
        dns.submit('%s.com' % name, rr.A, callback=callback, extra=domain)
        dns.submit('%s.net' % name, rr.A, callback=callback, extra=domain)
        dns.submit('%s.org' % name, rr.A, callback=callback, extra=domain)
        dns.submit('www.%s.com' % name, rr.A, callback=callback, extra=domain)
        dns.submit('www.%s.net' % name, rr.A, callback=callback, extra=domain)
        dns.submit('www.%s.org' % name, rr.A, callback=callback, extra=domain)
    dns.finish() # Wait for all DNS results.
    for domain in domains:
        name = domain.key().name()
        domain.count_chars()
        domain.set_substrings()
        print '%-20s %5s %5s %5s %-16s %-16s %-16s %s,%s,%s,%s' % (
            name, domain.length, domain.digits, domain.dashes,
            domain.com, domain.net, domain.org,
            domain.left1, domain.left6, domain.right6, domain.right1)


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    update_domains()


if __name__ == '__main__':
    main()
