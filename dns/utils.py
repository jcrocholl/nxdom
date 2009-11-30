def ip_to_int(ip):
    """
    >>> ip_to_int(None)
    0
    >>> ip_to_int('0.0.0.0')
    0
    >>> ip_to_int('1.2.3.4')
    16909060
    """
    if ip is None:
        return 0
    result = 0
    for part in ip.split('.'):
        result = (result << 8) + int(part)
    return result


def int_to_ip(value):
    """
    >>> int_to_ip(None)
    ''
    >>> int_to_ip(0)
    ''
    >>> int_to_ip(-1)
    '-1'
    >>> int_to_ip(16909060)
    '1.2.3.4'
    """
    if not value:
        return ''
    if value < 0:
        return str(value)
    return '.'.join((
        str((value >> 24) & 0xFF),
        str((value >> 16) & 0xFF),
        str((value >> 8) & 0xFF),
        str(value & 0xFF)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
