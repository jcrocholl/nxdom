#!/usr/bin/env python

import sys
import subprocess
from optparse import OptionParser


def load_app_yaml():
    input = open('app.yaml', 'r')
    lines = input.readlines()
    input.close()
    while lines and not lines[-1].strip():
        lines.pop(-1)
    return lines


def update_app_yaml(lines, **kwargs):
    output = open('app.yaml', 'w')
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            argname = key.strip().replace('-', '_')
            if argname in kwargs:
                line = key + ': ' + kwargs[argname] + '\n'
        output.write(line)
    output.close()


def attempt(command):
    print command
    returncode = subprocess.call(command.split())
    if returncode:
        print "failed with return code", returncode
        sys.exit(returncode)


def main():
    usage = "usage: %prog [options] [version]"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()
    if not args:
        options.version = 'master'
    elif len(args) == 1:
        options.version = args[0]
    else:
        parser.error("Too many command line arguments.")
    app_yaml = load_app_yaml()
    update_app_yaml(app_yaml, version=options.version)
    attempt('./manage.py update')
    update_app_yaml(app_yaml)


if __name__ == '__main__':
    sys.exit(main())
