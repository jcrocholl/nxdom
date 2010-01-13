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
    com = db.IntegerProperty(default=0)
    timestamp = db.DateTimeProperty()


class Suffix(db.Expando):
    """
    Count all domains in the datastore that end with the same suffix
    as the key name of the counter.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    com = db.IntegerProperty(default=0)
    timestamp = db.DateTimeProperty()


# Deprecated since 2010-01-12
class DotComPrefix(db.Model):
    """
    Count all domains in the datastore that start with the same prefix
    as the key name of the counter, and have existing .com DNS.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()


# Deprecated since 2010-01-12
class DotComSuffix(db.Model):
    """
    Count all domains in the datastore that end with the same suffix
    as the key name of the counter, and have existing .com DNS.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()
