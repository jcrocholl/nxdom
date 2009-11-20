import random

from google.appengine.ext import db

from domains.models import Domain, DOMAIN_CHARS, MAX_NAME_LENGTH


def random_domains(keys_only=False):
    query = Domain.all(keys_only=keys_only)
    length = random.choice([1, 2, MAX_NAME_LENGTH])
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
    return query, description
