import random

DOMAIN_CHARS = 'abcdefghijklmnopqrstuvwxyz-0123456789'


def increment_prefix(chars):
    return chars[:-1] + chr(ord(chars[-1]) + 1)


def random_prefix(length=3):
    return ''.join([random.choice(DOMAIN_CHARS) for index in range(length)])
