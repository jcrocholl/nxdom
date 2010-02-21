from google.appengine.ext import db

TOP_LEVEL_DOMAINS = """
com net org biz info
am at
be by
ca ch
de
es eu
fm
in io is it
la li ly
me mobi
name
ru
se
tel to travel tv
us
""".split()

# Omitting nu, ph, st, ws because they don't seem to have NXDOMAIN.
# Omitting ag, ck, ms, sh, sy, th because they have few domains.


class Lookup(db.Expando):
    """
    The datastore key name is the domain name, without top level.

    Since 2010-01-02, this model inherits from Expando to flexibly add
    or remove top level domains. Each TLD property stores the
    authority name server as string backwards like 'com.1and1.ns57'
    for better sorting, or something like 'status=rcodeservfail' or
    'timeout=20' (in seconds). If a domain property is missing, this
    indicates NXDOMAIN.
    """
    backwards = db.StringProperty(required=True)  # For suffix matching.
    timestamp = db.DateTimeProperty(required=True)  # Created or updated.
