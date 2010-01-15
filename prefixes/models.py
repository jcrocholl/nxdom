from datetime import datetime

from google.appengine.ext import db

from domains.models import Domain


class Prefix(db.Expando):
    """
    Count all domains in the datastore that start with the same prefix
    as the key name of the counter.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    com = db.IntegerProperty()
    percentage = db.FloatProperty()
    timestamp = db.DateTimeProperty()


class Suffix(db.Expando):
    """
    Count all domains in the datastore that end with the same suffix
    as the key name of the counter.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    com = db.IntegerProperty()
    percentage = db.FloatProperty()
    timestamp = db.DateTimeProperty()
