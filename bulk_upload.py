#!/usr/bin/env python

import os
import sys
import getpass
import datetime

from common.appenginepatch.aecmd import setup_env
setup_env()

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub

from domains.models import Domain, Whois

BATCH_SIZE = 200


def auth_func():
    return open('.passwd').read().split(':')


def load_names(filename, resume=None):
    names = []
    for line in open(filename):
        for name in line.split():
            if name >= resume:
                names.append(name)
    return names


def put(objects):
    if not objects:
        return
    print "Uploading %d objects (%s to %s):" % (
        len(objects), objects[0].key().name(), objects[-1].key().name())
    db.put(objects)
    del objects[:]


def bulk_upload(date, tld, names):
    domains = []
    whois = []
    for name in names:
        domains.append(Domain(key_name=name, backwards=name[::-1],
                              timestamp=datetime.datetime.now()))
        whois.append(Whois(key_name=name + '.' + tld,
                           expiration=date, timestamp=date))
        if len(domains) >= BATCH_SIZE:
            put(domains)
            put(whois)
    put(domains)
    put(whois)


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--resume', metavar='<name>',
                      help="resume upload, starting from this name")
    parser.add_option('--server', metavar='<hostname>',
                      default='scoretool.appspot.com',
                      help="connect to a different server")
    (options, args) = parser.parse_args()
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api', auth_func, options.server)
    for filename in args:
        names = load_names(filename, options.resume)
        names.sort()
        date, tld, ext = os.path.basename(filename).split('.', 2)
        year, month, day = date.split('-')
        date = datetime.date(int(year), int(month), int(day))
        bulk_upload(date, tld, names)


if __name__ == '__main__':
    main()
