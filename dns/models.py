from google.appengine.ext import db

TOP_LEVEL_DOMAINS = """
com net org biz info
ag am at
be by
ch ck
de
es eu
fm
in io is it
la li ly
me mobi ms
name
ru
se sh sy
tel th to travel tv
us
""".split()

# Omitting nu, ph, st, ws because they don't seem to have NXDOMAIN.


class UpgradeStringProperty(db.IntegerProperty):

    def validate(self, value):
        return unicode(value) if value else u''



class Lookup(db.Expando):
    """
    The datastore key name is the domain name, without top level.

    IP address fields use 0 (zero) for NXDOMAIN because None is
    returned for missing properties.

    Some updates on 2010-01-01 use negative numbers for 60 bit hashes of
    the SOA server name.

    Since 2010-01-02, this model inherits from Expando to flexibly add
    more top level domains. Each property stores the authority name
    server as string backwards, e.g. com.1and1.ns1 for better sorting.
    """
    backwards = db.StringProperty(required=True) # For suffix matching.
    timestamp = db.DateTimeProperty(required=True) # Created or updated.
    com = UpgradeStringProperty()
    net = UpgradeStringProperty()
    org = UpgradeStringProperty()
    biz = UpgradeStringProperty()
    info = UpgradeStringProperty()
