from google.appengine.ext import db

TOP_LEVEL_DOMAINS = 'com net org biz info'.split()


class Lookup(db.Model):
    """
    The datastore key name is the domain name, without top level.

    IP address fields use 0 (zero) for NXDOMAIN because None is
    returned for missing properties.

    Updates since 2010-01-01 use negative numbers for 60 bit hashes of
    the SOA server name, see tools/update_dns.py.
    """
    backwards = db.StringProperty(required=True) # For suffix matching.
    timestamp = db.DateTimeProperty(required=True) # Created or updated.
    com = db.IntegerProperty(indexed=False)
    net = db.IntegerProperty(indexed=False)
    org = db.IntegerProperty(indexed=False)
    biz = db.IntegerProperty(indexed=False)
    info = db.IntegerProperty(indexed=False)
