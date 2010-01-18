import logging
import random
import math

from google.appengine.ext import db

from domains.models import Domain, MAX_NAME_LENGTH


def random_prefix(position='left', length_choices=[1, 2, 3, 4, 5, 6]):
    from prefixes import popular
    length = random.choice(length_choices)
    if position == 'left':
        prefixes = popular.POPULAR_PREFIXES[max(2, length)]
    elif position == 'right':
        prefixes = popular.POPULAR_SUFFIXES[max(2, length)]
    prefix = prefixes[int(len(prefixes) * math.sqrt(random.random()))]
    return prefix[:length]


def random_letters(length, letter_choices='abcdefghijklmnopqrstuvwxyz'):
    return ''.join([random.choice(letter_choices) for index in range(length)])


def random_name(position='left', length=MAX_NAME_LENGTH):
    name = random_prefix(position=position)
    if position == 'left' and len(name) < length:
        name = name + random_letters(length - len(name))
    elif position == 'right' and len(name) < length:
        name = random_letters(length - len(name)) + name
    return name


class Selector:

    def __init__(self,
                 position_choices=['left', 'right'],
                 order_choices=['ascending', 'descending']):
        self.position = random.choice(position_choices)
        self.order = random.choice(order_choices)
        if self.position == 'left' and self.order == 'descending':
             # Don't use corrupt descending __key__ indexes.
            self.order = 'ascending'
        self.name = random_name(position=self.position)

    def description(self):
        description = []
        if self.order == 'ascending':
            description.append('after')
        elif self.order == 'descending':
            description.append('before')
        description.append(self.name)
        if self.position == 'right':
            description.append('backwards')
        return ' '.join(description)

    def select(self, model, keys_only=False):
        query = model.all(keys_only=keys_only)
        if self.position == 'left':
            field = '__key__'
            start = db.Key.from_path(model.kind(), self.name)
        elif self.position == 'right':
            field = 'backwards'
            start = self.name[::-1]
        if self.order == 'ascending':
            query.order(field)
            query.filter(field + ' >', start)
        elif self.order == 'descending':
            query.order('-' + field)
            query.filter(field + ' <', start)
        return query

    def fetch_names(self, model, count):
        query = self.select(model, keys_only=True)
        names = [key.name() for key in query.fetch(count)]
        if (self.position == 'left' and self.order == 'ascending' and
            names and names[0].startswith('zzzzz')):
            logging.warning('second attempt after getting zzzzz')
            names = [key.name() for key in query.fetch(count)]
        if (self.position == 'left' and self.order == 'ascending' and
            names and names[0].startswith('zzzzz')):
            logging.warning('third attempt after getting zzzzz')
            names = [key.name() for key in query.fetch(count)]
        if not names:
            return []
        if self.position == 'left':
            compare = cmp
        elif self.position == 'right':
            compare = lambda a, b: cmp(a[::-1], b[::-1])
        if self.order == 'ascending':
            assert compare(names[0], self.name) >= 0 # ascending index
        elif self.order == 'descending':
            assert compare(names[0], self.name) <= 0 # descending index
            names.reverse()
        for index in range(1, len(names)):
            assert compare(names[index - 1], names[index]) < 0 # sorted
        return names

    def truncate_range(self, a, b):
        """
        Truncate two lists of names to the same range if necessary.
        """
        if not a or not b:
            return
        if self.position == 'left':
            compare = cmp
        elif self.position == 'right':
            compare = lambda a, b: cmp(a[::-1], b[::-1])
        if self.order == 'ascending':
            if compare(a[-1], b[-1]) > 0:
                while a and compare(a[-1], b[-1]) > 0:
                    del a[-1]
            else:
                while b and compare(a[-1], b[-1]) < 0:
                    del b[-1]
        elif self.order == 'descending':
            if compare(a[0], b[0]) < 0:
                while a and compare(a[0], b[0]) < 0:
                    del a[0]
            else:
                while b and compare(a[0], b[0]) > 0:
                    del b[0]


def demo():
    for index in range(10):
        selector = Selector()
        names = selector.fetch_names(Domain, 100)
        print selector.description() + ':'
        print ' '.join(names)
        print
