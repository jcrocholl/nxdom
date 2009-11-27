from google.appengine.ext import db

TOP_LEVEL_DOMAINS = 'com net org biz info'.split()


class Lookup(db.Model):
    """
    The datastore key name is the domain name, without top level.
    """
    backwards = db.StringProperty(required=True) # For suffix matching.
    timestamp = db.DateTimeProperty(required=True) # Created or updated.
    com = db.IntegerProperty() # Use 0 (zero) for NXDOMAIN because None
    net = db.IntegerProperty() # is returned for missing properties.
    org = db.IntegerProperty()
    biz = db.IntegerProperty()
    info = db.IntegerProperty()
