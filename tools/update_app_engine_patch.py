#!/usr/bin/env python

FOLDERS = "common blueprintcss".split()

import os, sys


def system(command):
    print command
    status = os.system(command)
    if status:
        print "failed with exit code %d" % status
        sys.exit(status)


for folder in FOLDERS:
    if os.path.exists(folder):
        system('rm -rf %s' % folder)
    system('cp -rf ../app-engine-patch-sample/%s .' % folder)
