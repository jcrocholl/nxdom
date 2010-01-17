#!/usr/bin/env python

# Setup project environment in the parent directory.
import os
import sys
sys.path[0] = os.path.dirname(sys.path[0])
from common.appenginepatch.aecmd import setup_env
setup_env()

from google.appengine.ext import db
from google.appengine.ext.remote_api import remote_api_stub

from prefixes.models import Prefix, Suffix
from tools.retry import retry


def fetch_file(Model, length):
    kind = Model.kind()
    filename = '%ses.%d.txt' % (kind.split('_')[-1], length)
    outfile = open(filename, 'w')
    start = db.Key.from_path(kind, '-')
    while True:
        query = Model.all().filter('length', length).order('__key__')
        query.filter('__key__ >', start)
        prefixes = retry(query.fetch, 1000)
        for prefix in prefixes:
            name = prefix.key().name()
            if name.startswith('.'):
                continue
            if kind == 'prefixes_suffix':
                name = name[::-1]
            outfile.write('%d %s\n' % (prefix.com, name))
        if len(prefixes) < 1000:
            break
        start = prefixes[-1].key()
    outfile.close()


def auth_func():
    return open('.passwd').read().split(':')


if __name__ == '__main__':
    remote_api_stub.ConfigureRemoteDatastore(
        'scoretool', '/remote_api_hidden', auth_func, 'www.nxdom.com')
    for length in range(2, 7):
        fetch_file(Prefix, length)
        fetch_file(Suffix, length)
