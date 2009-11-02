from google.appengine.ext import db


class Config(db.Model):
  name = db.StringProperty(required=True)
  num_shards = db.IntegerProperty(required=True, default=20)


class Shard(db.Model):
  name = db.StringProperty(required=True)
  count = db.IntegerProperty(required=True, default=0)


class Prefix(db.Model):
  """
  Count all domains in the datastore that start with the same prefix
  as the key name of the counter.
  """
  length = db.IntegerProperty(required=True)
  count = db.IntegerProperty(required=True, default=0)
