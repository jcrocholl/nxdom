from google.appengine.ext import db

TOP_LEVEL_DOMAINS = 'com net org biz info'.split()


class Lookup(db.Model):
    """
    The datastore key name is the domain name, without top level.
    """
    backwards = db.StringProperty(required=True) # For suffix matching.
    timestamp = db.DateTimeProperty(required=True) # Created or updated.
    com = db.BooleanProperty() # True if name.com has IP address.
    net = db.BooleanProperty()
    org = db.BooleanProperty()
    biz = db.BooleanProperty()
    info = db.BooleanProperty()
