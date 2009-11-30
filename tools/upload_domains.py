#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

import time
import datetime

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.api.datastore_errors import Timeout

from domains.models import Domain, MAX_NAME_LENGTH
from utils.retry import retry_objects

BATCH_SIZE = 100


def auth_func():
    return open('.passwd').read().split(':')


def bulk_upload(lines):
    domains = []
    previous = ''
    for line in lines:
        name = line.strip()
        if not name:
            continue
        if '.' in name:
            name, tld = line.split('.')
        if len(name) > MAX_NAME_LENGTH:
            continue
        if name != previous:
            previous = name
            domain = Domain(key_name=name)
            domain.before_put()
            print '%s  %-16s %3d%3d%3d %3d%3d%3d%3d' % (
                domain.timestamp.strftime('%Y-%m-%d %H:%M'), name,
                domain.length, domain.digits, domain.dashes,
                domain.english, domain.spanish, domain.french, domain.german),
            if domain.length > 6 and not (
                domain.english or domain.spanish or
                domain.french or domain.german):
                print 'unreadable'
            else:
                domains.append(domain)
                print
        if len(domains) >= BATCH_SIZE:
            retry_objects(db.put, domains)
            domains = []
    # After the last loop, upload the rest.
    if domains:
        retry_objects(db.put, domains)


def upload_from_file(filename, resume=None):
    lines = open(filename).readlines()
    lines.sort()
    if resume:
        while lines[0] < resume:
            lines.pop(0)
    bulk_upload(lines)


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
    for filename in args:
        upload_from_file(filename, options.resume)
        options.resume = None # Only for the first filename.


if __name__ == '__main__':
    main()
