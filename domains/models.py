from datetime import datetime

from google.appengine.ext import db

from dictionaries import english


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

    length = db.IntegerProperty()
    digits = db.IntegerProperty()
    dashes = db.IntegerProperty()

    # Prefixes.
    left1 = db.StringProperty()
    left2 = db.StringProperty()
    left3 = db.StringProperty()
    left4 = db.StringProperty()
    left5 = db.StringProperty()
    left6 = db.StringProperty()

    # Suffixes.
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
        Automatically populate some properties.
        """
        if self.is_saved():
            return
        self.timestamp = datetime.now()
        self.count_chars()
        self.set_substrings()

    def count_chars(self):
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

    def set_substrings(self):
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

    def check_dictionaries(self, keyword, position):
        if position == 'left':
            self.rest = self.key().name()[len(keyword):]
        if position == 'right':
            self.rest = self.key().name()[:-len(keyword)]
        if self.rest in english.SCOWL10:
            self.scowl = 4
        elif self.rest in english.SCOWL20:
            self.scowl = 3
        elif self.rest in english.SCOWL35:
            self.scowl = 2
        elif self.rest in english.SCOWL50:
            self.scowl = 1
        else:
            self.scowl = 0


class Whois(db.Model):
    """
    The datastore key name is "domain.tld".
    """
    timestamp = db.DateProperty()
    expiration = db.DateProperty() # Or None if not found.


class Dns(db.Model):
    """
    The datastore key name is "domain.tld".
    """
    timestamp = db.DateProperty()
    ip = db.StringProperty() # Or None if not found.
