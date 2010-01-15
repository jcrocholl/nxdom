from datetime import datetime

from google.appengine.ext import db

from domains.models import Domain


class Prefix(db.Expando):
    """
    Count all domains in the datastore that start with the same
    prefix. The key name is the prefix, with a leading dot and
    optional property 'resume' if incomplete.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    com = db.IntegerProperty()
    percentage = db.FloatProperty()
    timestamp = db.DateTimeProperty()


class Suffix(db.Expando):
    """
    Count all domains in the datastore that end with the same suffix.
    The key name is the suffix backwards, with a leading dot
    and optional property 'resume' if incomplete.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    com = db.IntegerProperty()
    percentage = db.FloatProperty()
    timestamp = db.DateTimeProperty()
