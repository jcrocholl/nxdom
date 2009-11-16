def increment_prefix(chars):
    return chars[:-1] + chr(ord(chars[-1]) + 1)
