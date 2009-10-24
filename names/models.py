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
    The name is used as the datastore key.
    """
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

    com_dns_checked = db.DateTimeProperty()
    net_dns_checked = db.DateTimeProperty()
    org_dns_checked = db.DateTimeProperty()

    com_dns_ip = db.StringProperty()
    net_dns_ip = db.StringProperty()
    org_dns_ip = db.StringProperty()

    com_whois_checked = db.DateTimeProperty()
    net_whois_checked = db.DateTimeProperty()
    org_whois_checked = db.DateTimeProperty()

    com_whois_expiration = db.DateTimeProperty()
    net_whois_expiration = db.DateTimeProperty()
    org_whois_expiration = db.DateTimeProperty()

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
            chars.reverse()
            self.backwards = ''.join(chars)
            self.length = self.letters + self.digits + self.dashes


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
