from datetime import datetime

from google.appengine.ext import db


class BaseModel(db.Model):
    def before_put(self):
        pass

    def after_put(self):
        pass

    def put(self):
        self.before_put()
        super(BaseModel, self).put()
        self.after_put()


class Idea(BaseModel):
    """
    The name is also used as the datastore key.
    """
    name = db.StringProperty()
    backwards = db.StringProperty()
    created = db.DateTimeProperty()
    updated = db.DateTimeProperty()

    length = db.IntegerProperty()
    syllables = db.IntegerProperty()
    letters = db.IntegerProperty()
    dashes = db.IntegerProperty()
    digits = db.IntegerProperty()

    score_pairs = db.FloatProperty()
    score_triples = db.FloatProperty()
    score_words = db.FloatProperty()

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
                    continue
                chars.append(char)
            self.length = self.letters + self.digits + self.dashes
            self.name = ''.join(chars)
            chars.reverse()
            self.backwards = ''.join(chars)

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
