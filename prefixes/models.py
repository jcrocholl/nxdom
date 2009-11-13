from datetime import datetime

from google.appengine.ext import db

from domains.models import Domain


def count_domains(field, value):
    result = 0
    previous = None
    while True:
        keys = Domain.all(keys_only=True)
        keys.filter(field, value)
        keys.order('__key__')
        if previous:
            keys.filter('__key__ >', previous)
        keys = keys.fetch(1000)
        result += len(keys)
        if len(keys) < 1000:
            return result
        previous = keys[-1]


class Prefix(db.Model):
    """
    Count all domains in the datastore that start with the same prefix
    as the key name of the counter.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()

    def count_domains(self):
        name = self.key().name()
        field = 'left%d' % len(name)
        self.count = count_domains(field, name)
        self.timestamp = datetime.now()


class Suffix(db.Model):
    """
    Count all domains in the datastore that end with the same suffix
    as the key name of the counter.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()

    def count_domains(self):
        name = self.key().name()
        field = 'right%d' % len(name)
        self.count = count_domains(field, name)
        self.timestamp = datetime.now()


class DotComPrefix(db.Model):
    """
    Count all domains in the datastore that start with the same prefix
    as the key name of the counter, and have existing .com DNS.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()


class DotComSuffix(db.Model):
    """
    Count all domains in the datastore that end with the same suffix
    as the key name of the counter, and have existing .com DNS.
    """
    length = db.IntegerProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)
    timestamp = db.DateTimeProperty()
