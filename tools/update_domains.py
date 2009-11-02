#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

import time
import getpass
import datetime

import ADNS
from adns import rr

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from domains.models import Domain

BATCH_SIZE = 400
MAX_ATTEMPTS = 5
MAX_NAME_LENGTH = 16
DNS_HIJACKERS = '208.67.219.132'.split()


def auth_func():
    return open('.passwd').read().split(':')


def put_batch(objects):
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


def delete_batch(objects):
    if not objects:
        return
    for attempt in range(MAX_ATTEMPTS):
        if attempt:
            print "Attempt %d of %d will start in %d seconds." % (
                attempt + 1, MAX_ATTEMPTS, attempt)
            time.sleep(attempt)
        print "Deleting %d objects (%s to %s):" % (
            len(objects), objects[0].key().name(), objects[-1].key().name())
        try:
            db.delete(objects)
            break
        except Timeout:
            print "*** Timeout ***"
            if attempt + 1 == MAX_ATTEMPTS:
                sys.exit(1)
    del objects[:]


def callback(answer, qname, rr, flags, domain):
    # print qname, answer
    ip_list = list(answer[3])
    ip_list.sort()
    ip = ip_list[0] if ip_list else None
    if ip in DNS_HIJACKERS:
        ip = None
    if ip:
        setattr(domain, qname[-3:], ip)


def update_domains(domains):
    dns = ADNS.QueryEngine()
    for domain in domains:
        name = domain.key().name()
        if len(name) > MAX_NAME_LENGTH:
            continue # No DNS lookup, this name will be deleted anyway.
        domain.com = None
        domain.net = None
        domain.org = None
        dns.submit('%s.com' % name, rr.A, callback=callback, extra=domain)
        dns.submit('%s.net' % name, rr.A, callback=callback, extra=domain)
        dns.submit('%s.org' % name, rr.A, callback=callback, extra=domain)
        dns.submit('www.%s.com' % name, rr.A, callback=callback, extra=domain)
        dns.submit('www.%s.net' % name, rr.A, callback=callback, extra=domain)
        dns.submit('www.%s.org' % name, rr.A, callback=callback, extra=domain)
    print "Waiting for DNS results..."
    dns.finish()
    domains_put = []
    domains_delete = []
    for domain in domains:
        name = domain.key().name()
        if len(name) > MAX_NAME_LENGTH:
            print '%s %s is too long (%d), deleting' % (
                domain.timestamp.strftime('%Y-%m-%d %H:%M'), name, len(name))
            if domain.is_saved():
                domains_delete.append(domain)
            continue
        if domain.com and domain.net and domain.org:
            print '%s %s has DNS for .com .net .org, deleting' % (
                domain.timestamp.strftime('%Y-%m-%d %H:%M'), name)
            if domain.is_saved():
                domains_delete.append(domain)
            continue
        domain.count_chars()
        domain.set_substrings()
        print '%s %-17s %5s %5s %5s %-16s %-16s %-16s %s,%s,%s,%s' % (
            domain.timestamp.strftime('%Y-%m-%d %H:%M'), name,
            domain.length, domain.digits, domain.dashes,
            domain.com, domain.net, domain.org,
            domain.left1, domain.left6, domain.right6, domain.right1)
        domain.timestamp = datetime.datetime.now()
        domains_put.append(domain)
    if domains_put:
        put_batch(domains_put)
    if domains_delete:
        delete_batch(domains_delete)


def update_server_domains():
    while True:
        domains = Domain.all().order('timestamp').fetch(BATCH_SIZE)
        update_domains(domains)


def bulk_upload(date, lines):
    domains = []
    previous = ''
    for line in lines:
        line = line.strip()
        if not line:
            continue
        name, tld = line.split('.')
        if len(name) > MAX_NAME_LENGTH:
            continue
        if name != previous:
            domain = Domain(key_name=name, backwards=name[::-1],
                            timestamp=datetime.datetime.now())
            domain.before_put()
            domains.append(domain)
        previous = name
        if len(domains) >= BATCH_SIZE:
            update_domains(domains)
    # After the last loop, upload the rest.
    if domains:
        update_domains(domains)


def upload_from_file(filename, resume=None):
    date, ext = os.path.basename(filename).split('.', 1)
    if date[2] == date[5] == '-':
        month, day, year = date.split('-')
    else:
        year, month, day = date.split('-')
    date = datetime.date(int(year), int(month), int(day))
    lines = open(filename).readlines()
    lines.sort()
    if resume:
        while lines[0] < resume:
            lines.pop(0)
    bulk_upload(date, lines)


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    parser.add_option('--resume', metavar='<name>',
                      help="resume upload, starting from this name")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    if not args:
        update_server_domains()
    else:
        for filename in args:
            upload_from_file(filename, options.resume)
            options.resume = None # Only for the first filename.


if __name__ == '__main__':
    main()