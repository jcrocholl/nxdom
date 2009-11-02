from google.appengine.ext import db


class Prefix(db.Model):
  """
  Count all domains in the datastore that start with the same prefix
  as the key name of the counter.
  """
  length = db.IntegerProperty(required=True)
  count = db.IntegerProperty(required=True, default=0)
  timestamp = db.DateTimeProperty()
