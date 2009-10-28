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

BATCH_SIZE = 400


def auth_func():
    return open('.passwd').read().split(':')


def put(objects):
    if not objects:
        return
    print "Uploading %d objects (%s to %s):" % (
        len(objects), objects[0].key().name(), objects[-1].key().name())
    db.put(objects)
    del objects[:]


def bulk_upload(date, lines):
    objects = []
    previous = ''
    for line in lines:
        line = line.strip()
        if not line:
            continue
        name, tld = line.split('.')
        if name != previous:
            objects.append(Domain(key_name=name, backwards=name[::-1],
                                  timestamp=datetime.datetime.now()))
        previous = name
        objects.append(Whois(key_name=line, expiration=date, timestamp=date))
        if len(objects) >= BATCH_SIZE:
            put(objects)
    put(objects)


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
        date, ext = os.path.basename(filename).split('.')
        month, day, year = date.split('-')
        date = datetime.date(int(year), int(month), int(day))
        lines = open(filename).readlines()
        lines.sort()
        if filename == args[0] and options.resume:
            while lines[0] < options.resume:
                lines.pop(0)
        bulk_upload(date, lines)


if __name__ == '__main__':
    main()
