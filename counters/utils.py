import random

from google.appengine.ext import db
from google.appengine.api import memcache

from counters.models import Shard, Config


def get_count(name):
  """
  Retrieve the value for a given sharded counter.
  """
  total = memcache.get(name)
  if total is None:
    total = 0
    for counter in Shard.all().filter('name = ', name):
      total += counter.count
    memcache.add(name, str(total), 60)
  return total


def increment(name, delta=1):
  """
  Increment the value for a given sharded counter.
  """
  config = Config.get_or_insert(name, name=name)
  def txn():
    index = random.randint(1, config.num_shards)
    shard_name = name + str(index)
    counter = Shard.get_by_key_name(shard_name)
    if counter is None:
      counter = Shard(key_name=shard_name, name=name)
    counter.count += delta
    counter.put()
  db.run_in_transaction(txn)
  memcache.incr(name, delta=delta)


def increase_shards(name, num):
  """
  Increase the number of shards for a given sharded counter.
  Will never decrease the number of shards.
  """
  config = Config.get_or_insert(name, name=name)
  def txn():
    if config.num_shards < num:
      config.num_shards = num
      config.put()
  db.run_in_transaction(txn)
