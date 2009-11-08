from datetime import datetime

from google.appengine.ext import db

from dictionaries.english import score_scowl_substrings
from readability.english import score_readability


class BaseModel(db.Model):

    @classmethod
    def get_or_insert_with_flag(cls, key_name, **kwds):
        def txn():
            created = False
            entity = cls.get_by_key_name(key_name)
            if entity is None:
                created = True
                entity = cls(key_name=key_name, **kwds)
                entity.put()
            return (entity, created)
        return db.run_in_transaction(txn)

    def before_put(self):
        pass

    def after_put(self):
        pass

    def put(self):
        self.before_put()
        super(BaseModel, self).put()
        self.after_put()


class Domain(BaseModel):
    """
    The datastore key name is the domain name, without top level.
    """
    backwards = db.StringProperty() # For suffix matching, name[::-1].
    timestamp = db.DateTimeProperty() # Automatically set in before_put.

    # DNS lookups.
    com = db.StringProperty()
    net = db.StringProperty()
    org = db.StringProperty()

    # Character counts.
    length = db.IntegerProperty()
    digits = db.IntegerProperty()
    dashes = db.IntegerProperty()

    # Linguistic quality measurements.
    scowl = db.IntegerProperty()
    english = db.IntegerProperty()

    # Prefixes for equality filters.
    left1 = db.StringProperty()
    left2 = db.StringProperty()
    left3 = db.StringProperty()
    left4 = db.StringProperty()
    left5 = db.StringProperty()
    left6 = db.StringProperty()

    # Suffixes for equality filters.
    right1 = db.StringProperty()
    right2 = db.StringProperty()
    right3 = db.StringProperty()
    right4 = db.StringProperty()
    right5 = db.StringProperty()
    right6 = db.StringProperty()

    def __unicode__(self):
        return self.key().name()

    def get_absolute_url(self):
        return reverse('names.views.detail', args=[self.key().name()])

    def before_put(self):
        """
        Automatically update most properties.
        """
        self.update_counts()
        self.update_scowl()
        self.update_english()
        self.update_substrings()
        self.timestamp = datetime.now()

    def update_counts(self):
        """
        Count digits and dashes.
        """
        name = self.key().name()
        self.length = len(name)
        self.digits = self.dashes = 0
        for char in name:
            if '0' <= char <= '9':
                self.digits += 1
            elif char == '-':
                self.dashes += 1

    def update_scowl(self):
        self.scowl = score_scowl_substrings(self.key().name())

    def update_english(self):
        self.english = score_readability(self.key().name())

    def update_substrings(self):
        """
        Set substrings for fast index matching.
        """
        name = self.key().name()
        length = len(name)
        self.backwards = name[::-1]
        self.left1 = name[:1] if length >= 1 else None
        self.left2 = name[:2] if length >= 2 else None
        self.left3 = name[:3] if length >= 3 else None
        self.left4 = name[:4] if length >= 4 else None
        self.left5 = name[:5] if length >= 5 else None
        self.left6 = name[:6] if length >= 6 else None
        self.right1 = name[-1:] if length >= 1 else None
        self.right2 = name[-2:] if length >= 2 else None
        self.right3 = name[-3:] if length >= 3 else None
        self.right4 = name[-4:] if length >= 4 else None
        self.right5 = name[-5:] if length >= 5 else None
        self.right6 = name[-6:] if length >= 6 else None


class Whois(db.Model):
    """
    The datastore key name is "domain.tld".
    """
    timestamp = db.DateProperty()
    expiration = db.DateProperty() # Or None if not found.
