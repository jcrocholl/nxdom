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
    The name is also used as the datastore key.
    """
    name = db.StringProperty() # Without top level domain and dots.
    backwards = db.StringProperty() # For suffix matching, name[::-1].
    created = db.DateTimeProperty() # Automatically set in before_put.
    updated = db.DateTimeProperty() # Automatically set in before_put.

    # Domain expiration dates, according to whois.
    com_expiration = db.DateProperty()
    net_expiration = db.DateProperty()
    org_expiration = db.DateProperty()

    def __unicode__(self):
        return self.key().name()

    def get_absolute_url(self):
        return reverse('names.views.detail', args=[self.key().name()])

    def before_put(self):
        """
        Automatically populate some properties.
        """
        self.updated = datetime.now()
        if not self.is_saved():
            self.created = self.updated
            self.name = self.key().name()
            self.backwards = self.name[::-1]

    def count_chars(self):
        self.len = len(self.name)
        self.letters = self.digits = self.dashes = 0
        chars = []
        for char in self.key().name():
            if 'a' <= char <= 'z':
                self.letters += 1
            elif '0' <= char <= '9':
                self.digits += 1
            elif char == '-':
                self.dashes += 1
            else:
                debug.error("%s contains bad char %s" % (self.name, char))

    def check_dictionaries(self, keyword, position):
        if position == 'left':
            self.rest = self.name[len(keyword):]
        if position == 'right':
            self.rest = self.name[:-len(keyword)]
        self.scowl10 = self.rest in english.SCOWL10
        self.scowl20 = self.rest in english.SCOWL20
        self.scowl35 = self.rest in english.SCOWL35
        self.scowl50 = self.rest in english.SCOWL50


class DnsCheck(db.Model):
    name = db.StringProperty()
    enam = db.StringProperty()
    tld = db.StringProperty()
    checked = db.DateTimeProperty(auto_now=True)
    ip = db.StringProperty()


class WhoisCheck(db.Model):
    name = db.StringProperty()
    enam = db.StringProperty()
    tld = db.StringProperty()
    checked = db.DateTimeProperty(auto_now=True)
    expiration = db.DateTimeProperty()
