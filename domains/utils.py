import random

from google.appengine.ext import db

from domains.models import Domain, DOMAIN_CHARS, MAX_NAME_LENGTH

ORDER_DESCRIPTIONS = {'length': 'shortest', '-english': 'most readable'}
POSITION_DESCRIPTIONS = {'left': 'start', 'right': 'end'}


def random_domains(keys_only=False,
                   length_choices=[1, 2, MAX_NAME_LENGTH],
                   position_choices=['left', 'right'],
                   order_choices=['length', '-english']):
    query = Domain.all(keys_only=keys_only)
    length = random.choice(length_choices)
    name = ''.join([random.choice(DOMAIN_CHARS) for i in range(length)])
    if length == MAX_NAME_LENGTH:
        key = db.Key.from_path('domains_domain', name)
        query.filter('__key__ >', key)
        description = "names that follow %s" % name
    else:
        position = random.choice(position_choices)
        order = random.choice(order_choices)
        query.filter('%s%d' % (position, len(name)), name)
        query.order(order)
        description = "%s names that %s with %s" % (
            ORDER_DESCRIPTIONS[order], POSITION_DESCRIPTIONS[position], name)
    return query, description
