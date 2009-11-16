import random

from google.appengine.ext import db

from domains.models import Domain, DOMAIN_CHARS, MAX_NAME_LENGTH


def get_random_domains(count, keys_only=False):
    query = Domain.all(keys_only=keys_only)
    length = random.choice([2, MAX_NAME_LENGTH])
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
    domains = query.fetch(count)
    if domains:
        return domains, description
    else: # Try again.
        return get_random_domains(count, keys_only)


def get_random_keys(count):
    return get_random_domains(count, keys_only=True)


def get_random_names(count):
    keys, description = get_random_keys(count)
    return [key.name() for key in keys], description
