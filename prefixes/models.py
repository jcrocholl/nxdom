from datetime import datetime

from google.appengine.ext import db

from domains.models import Domain


class Prefix(db.Model):
    """
    Count all domains in the datastore that start with the same prefix
    as the key name of the counter.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()


class Suffix(db.Model):
    """
    Count all domains in the datastore that end with the same suffix
    as the key name of the counter.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()


class DotComPrefix(db.Model):
    """
    Count all domains in the datastore that start with the same prefix
    as the key name of the counter, and have existing .com DNS.
    """
    length = db.IntegerProperty()
    count = db.IntegerProperty()
    timestamp = db.DateTimeProperty()

    def count_domains(self):
        prefix = self.key().name()
        self.length = len(prefix)
        field = 'left%d' % len(prefix)
        keys = Domain.all().order('com').order('__key__')
        keys.filter(field, prefix).filter('com !=', None)
        keys = keys.fetch(1000)
        self.count = len(keys)
        while len(keys) == 1000:
            previous = keys[-1]
            keys = Domain.all().order('com').order('__key__')
            keys.filter(field, prefix).filter('com !=', None)
            keys.filter('__key__ >', previous)
            keys = keys.fetch(1000)
            self.count += len(keys)
        self.timestamp = datetime.now()


class DotComSuffix(db.Model):
    """
    Count all domains in the datastore that end with the same suffix
    as the key name of the counter, and have existing .com DNS.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()
