import random

from google.appengine.ext import db

from domains.models import Domain, DOMAIN_CHARS, MAX_NAME_LENGTH
from prefixes import counts

ORDER_DESCRIPTIONS = {'length': 'shortest', '-english': 'most readable'}
POSITION_DESCRIPTIONS = {'left': 'start', 'right': 'end'}


def random_prefix_one():
    index = random.randint(1, counts.TOTAL)
    for c1 in DOMAIN_CHARS:
        index -= counts.ONE.get(c1, 0)
        if index <= 0:
            return c1
    return 'a'


def random_prefix(length=2):
    """
    Random domain name prefix, with adjusted probability for the first
    two characters.
    """
    if length == 1:
        return random_prefix_one()
    index = random.randint(1, counts.TOTAL)
    for c1 in DOMAIN_CHARS:
        for c2 in DOMAIN_CHARS:
            index -= counts.TWO.get(c1 + c2, 0)
            if index <= 0:
                result = c1 + c2
                while len(result) < length:
                    result += random.choice(DOMAIN_CHARS)
                return result


def random_domains(keys_only=False,
                   length_choices=[1, 2, MAX_NAME_LENGTH],
                   position_choices=['left', 'right'],
                   order_choices=['length', '-english']):
    query = Domain.all(keys_only=keys_only)
    length = random.choice(length_choices)
    name = random_prefix(length)
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
