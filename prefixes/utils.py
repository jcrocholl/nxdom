import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
DOMAIN_CHARS = LETTERS + DIGITS + '-'
DOMAIN_CHARS_NO_DASH = LETTERS + DIGITS


def increment_prefix(chars):
    return chars[:-1] + chr(ord(chars[-1]) + 1)


def random_prefix(length=3):
    if length < 1:
        return ''
    chars = [random.choice(DOMAIN_CHARS_NO_DASH)]
    while len(chars) < length:
        chars.append(random.choice(DOMAIN_CHARS))
    return ''.join(chars)
