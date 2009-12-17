from datetime import datetime

from google.appengine.ext import db

from languages import english, spanish, german, french
from languages.utils import word_score

MAX_NAME_LENGTH = 12
DOMAIN_CHARS = 'abcdefghijklmnopqrstuvwxyz-0123456789'
OBSOLETE_ATTRIBUTES = """
scowl com net org dns_com dns_net dns_org dns_timestamp
""".split()
CACHE_ATTRIBUTES = """
digits dashes
english spanish french german
prefix suffix score
com net org biz info
""".split()


class BaseModel(db.Expando):

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
    # For suffix matching, name[::-1].
    backwards = db.StringProperty()

    # Last update, automatically set in before_put.
    timestamp = db.DateTimeProperty()

    # Character counts.
    length = db.IntegerProperty()
    digits = db.IntegerProperty()
    dashes = db.IntegerProperty()

    # Linguistic quality measurements.
    english = db.FloatProperty()
    spanish = db.FloatProperty()
    french = db.FloatProperty()
    german = db.FloatProperty()

    # Popular prefixes and suffixes.
    prefix = db.FloatProperty()
    suffix = db.FloatProperty()

    # The highest score from languages and popular prefix / suffix.
    score = db.FloatProperty()

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
        self.update_language_scores()
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

    def language_scores_need_update(self):
        for lang in 'english spanish french german'.split():
            if not hasattr(self, lang):
                return True
            score = getattr(self, lang)
            if score is None or score < 0.0 or score >= 1.0:
                return True
        return False

    def update_language_scores(self):
        self.english = word_score(self.key().name(), english.TRIPLE_SCORES)
        self.spanish = word_score(self.key().name(), spanish.TRIPLE_SCORES)
        self.german = word_score(self.key().name(), german.TRIPLE_SCORES)
        self.french = word_score(self.key().name(), french.TRIPLE_SCORES)

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

    def to_cache(self):
        values = []
        for attr in CACHE_ATTRIBUTES:
            if hasattr(self, attr):
                values.append(str(getattr(self, attr)))
            else:
                values.append('None')
        return ' '.join(values)

    @classmethod
    def from_cache(cls, key, values):
        attributes = {}
        for attr, value in zip(CACHE_ATTRIBUTES, values.split()):
            if value == 'None':
                value = None
            elif value == 'True':
                value = True
            elif value == 'False':
                value = False
            elif '.' in value:
                value = float(value)
            else:
                value = int(value)
            attributes[attr] = value
        return cls(key_name=key, length=len(key), **attributes)
