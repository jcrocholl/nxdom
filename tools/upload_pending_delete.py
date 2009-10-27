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
DATE_REGEX = re.compile(r'(\d+)-(\d+)-(\d+)')


def upload(filename):
    month, day, year = DATE_REGEX.match(os.path.basename(filename)).groups()
    date = '%s-%s-%s' % (year, month, day)
    tld_names = {}
    for line in open(filename):
        domain = line.strip()
        if not '.' in domain:
            continue
        name, tld = domain.split('.')
        if tld not in TOP_LEVEL_DOMAINS:
            continue
        if tld not in tld_names:
            tld_names[tld] = []
        tld_names[tld].append(name)
    tlds = tld_names.keys()
    tlds.sort()
    for tld in tlds:
        names = tld_names[tld]
        # random.shuffle(names)
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
