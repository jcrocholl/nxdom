#!/usr/bin/env python

import sys
import os
import random
import urllib
import urllib2
import re


# POST_URL = 'http://localhost:8000/domains/'
POST_URL = 'http://scoretool.appspot.com/domains/'
TOP_LEVEL_DOMAINS = 'com net org'.split()
NAMES_PER_REQUEST = 200


def upload(filename):
    date, tld, ext = os.path.basename(filename).split('.', 2)
    names = []
    for line in open(filename):
        names.extend(line.split())
    while names:
        data = {
            'names': ' '.join(names[:NAMES_PER_REQUEST]),
            'com_expiration': '',
            'net_expiration': '',
            'org_expiration': '',
            'submit_names': 'submit'}
        data['%s_expiration' % tld] = date
        print data
        response = urllib2.urlopen(POST_URL, urllib.urlencode(data))
        if len(names) > NAMES_PER_REQUEST:
            names = names[NAMES_PER_REQUEST:]
        else:
            break


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        upload(filename)
