from datetime import datetime

from google.appengine.ext import db

from django.core.urlresolvers import reverse

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


class Domain(db.Model):
    """
    The datastore key name is the domain name, without top level.
    """
    # For suffix matching, name[::-1].
    backwards = db.StringProperty()

    # Last update, automatically set in before_put.
    timestamp = db.DateTimeProperty()

    # Character counts.
    length = db.IntegerProperty()
    digits = db.IntegerProperty(indexed=False)
    dashes = db.IntegerProperty(indexed=False)

    # Linguistic quality measurements.
    english = db.FloatProperty(indexed=False)
    spanish = db.FloatProperty(indexed=False)
    french = db.FloatProperty(indexed=False)
    german = db.FloatProperty(indexed=False)

    # Popular prefixes and suffixes.
    prefix = db.FloatProperty(indexed=False)
    suffix = db.FloatProperty(indexed=False)

    # The average score from prefix/suffix popularity and the best language.
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
        return reverse('domains.views.detail', args=[self.key().name()])

    def before_put(self):
        """
        Automatically update most properties.
        """
        self.delete_obsolete_attributes()
        self.update_counts()
        self.update_language_scores()
        self.update_popularity_scores()
        self.update_score()
        self.update_substrings()
        self.timestamp = datetime.now()

    def delete_obsolete_attributes(self):
        """
        Find and remove for obselete attributes from previous versions
        of the software.
        """
        for attr in OBSOLETE_ATTRIBUTES:
            if hasattr(self, attr):
                delattr(self, attr)

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
        from languages import english, spanish, german, french
        self.english = word_score(self.key().name(), english.TRIPLE_SCORES)
        self.spanish = word_score(self.key().name(), spanish.TRIPLE_SCORES)
        self.german = word_score(self.key().name(), german.TRIPLE_SCORES)
        self.french = word_score(self.key().name(), french.TRIPLE_SCORES)

    def popularity_scores_need_update(self):
        for attr in 'prefix suffix'.split():
            if not hasattr(self, attr):
                return True
            score = getattr(self, attr)
            if score is None or score < 0.0 or score > 1.0:
                return True
        return False

    def update_popularity_scores(self):
        from prefixes.popular import prefix_score, suffix_score
        self.prefix, self._best_prefix = prefix_score(self.key().name())
        self.suffix, self._best_suffix = suffix_score(self.key().name())

    def get_best_prefix(self):
        return self._best_prefix

    def get_best_suffix(self):
        return self._best_suffix

    def update_score(self):
        best_language = max(self.english, self.spanish,
                            self.french, self.german)
        self.score = (self.prefix + self.suffix + best_language) / 3

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
            if not hasattr(self, attr):
                continue
            value = getattr(self, attr)
            if isinstance(value, float):
                value = '%.6f' % value
            values.append('%s=%s' % (attr, value))
        return ' '.join(values)

    @classmethod
    def from_cache(cls, key, values):
        attributes = {}
        for pair in values.split():
            if '=' not in pair:
                raise ValueError(pair)
            attr, value = pair.split('=', 1)
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
