def reverse_name(fqdn):
    """
    >>> reverse_name('ns57.1and1.com')
    'com.1and1.ns57'
    """
    parts = fqdn.split('.')
    parts.reverse()
    return '.'.join(parts)


def status_name(status):
    """
    >>> import adns
    >>> status_name(adns.status.nxdomain)
    'nxdomain'
    """
    import adns
    return {
        adns.status.ok: 'ok',
        adns.status.nomemory: 'nomemory',
        adns.status.unknownrrtype: 'unknownrrtype',
        adns.status.systemfail: 'systemfail',
        adns.status.timeout: 'timeout',
        adns.status.allservfail: 'allservfail',
        adns.status.norecurse: 'norecurse',
        adns.status.invalidresponse: 'invalidresponse',
        adns.status.unknownformat: 'unknownformat',
        adns.status.rcodeservfail: 'rcodeservfail',
        adns.status.rcodeformaterror: 'rcodeformaterror',
        adns.status.rcodenotimplemented: 'rcodenotimplemented',
        adns.status.rcoderefused: 'rcoderefused',
        adns.status.rcodeunknown: 'rcodeunknown',
        adns.status.inconsistent: 'inconsistent',
        adns.status.prohibitedcname: 'prohibitedcname',
        adns.status.answerdomaininvalid: 'answerdomaininvalid',
        adns.status.invaliddata: 'invaliddata',
        adns.status.querydomainwrong: 'querydomainwrong',
        adns.status.querydomaininvalid: 'querydomaininvalid',
        adns.status.querydomaintoolong: 'querydomaintoolong',
        adns.status.nxdomain: 'nxdomain',
        adns.status.nodata: 'nodata',
        }.get(status, str(status))


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
