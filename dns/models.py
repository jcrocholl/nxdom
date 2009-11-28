from google.appengine.ext import db

TOP_LEVEL_DOMAINS = 'com net org biz info'.split()


class UpgradeIntegerProperty(db.IntegerProperty):

    def validate(self, value):
        if value is True:
            return -1
        elif value is False:
            return 0
        else:
            return value


class Lookup(db.Model):
    """
    The datastore key name is the domain name, without top level.

    IP address fields use 0 (zero) for NXDOMAIN because None is
    returned for missing properties. Previous Boolean values are
    upgraded as -1 and gradually replaced with IP addresses.
    """
    backwards = db.StringProperty(required=True) # For suffix matching.
    timestamp = db.DateTimeProperty(required=True) # Created or updated.
    com = UpgradeIntegerProperty()
    net = UpgradeIntegerProperty()
    org = UpgradeIntegerProperty()
    biz = UpgradeIntegerProperty()
    info = UpgradeIntegerProperty()
