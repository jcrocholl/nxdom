import random

from google.appengine.ext import db

from domains.models import Domain, DOMAIN_CHARS, MAX_NAME_LENGTH


def get_random_names(count):
    query = Domain.all(keys_only=True)
    length = random.choice([1, 2, 3, MAX_NAME_LENGTH])
    name = ''.join([random.choice(DOMAIN_CHARS) for i in range(length)])
    if length == MAX_NAME_LENGTH:
        key = db.Key.from_path('domains_domain', name)
        query.filter('__key__ >', key)
        description = "names that follow %s" % name
    else:
        position = random.choice(['left', 'right'])
        order = random.choice(['length', '-english'])
        query.filter('%s%d' % (position, len(name)), name)
        query.order(order)
        description = "%s names that %s with %s" % (
            'shortest' if order == 'length' else 'most readable',
            'start' if position == 'left' else 'end', name)
    keys = query.fetch(count)
    names = [key.name() for key in keys]
    if names:
        return names, description
    else: # Try again.
        return get_random_names(count)
