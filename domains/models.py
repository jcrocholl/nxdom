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

    def __unicode__(self):
        return self.key().name()

    def get_absolute_url(self):
        return reverse('names.views.detail', args=[self.key().name()])

    def before_put(self):
        """
        Automatically populate some properties.
        """
        if not self.is_saved():
            self.timestamp = datetime.now()
            self.backwards = self.key().name()[::-1]

    def count_chars(self):
        name = self.key().name()
        self.len = len(name)
        self.letters = self.digits = self.dashes = 0
        chars = []
        for char in name:
            if 'a' <= char <= 'z':
                self.letters += 1
            elif '0' <= char <= '9':
                self.digits += 1
            elif char == '-':
                self.dashes += 1
            else:
                debug.error("%s contains bad char %s" % (name, char))

    def check_dictionaries(self, keyword, position):
        if position == 'left':
            self.rest = self.key().name()[len(keyword):]
        if position == 'right':
            self.rest = self.key().name()[:-len(keyword)]
        self.scowl10 = self.rest in english.SCOWL10
        self.scowl20 = self.rest in english.SCOWL20
        self.scowl35 = self.rest in english.SCOWL35
        self.scowl50 = self.rest in english.SCOWL50


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
