from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from ragendja.template import render_to_response
from appenginepatcher import on_production_server

from google.appengine.ext import db

from domains.utils import random_prefix
from domains.models import MAX_NAME_LENGTH, Domain
from dns.models import Lookup
from prefixes.selectors import Selector, random_name

BATCH_SIZE = 100


def assert_missing(missing):
    keys = [db.Key.from_path('dns_lookup', domain.key().name())
            for domain in missing]
    for lookup in db.get(keys):
        assert lookup is None


def assert_obsolete(obsolete):
    for lookup in db.get(obsolete):
        assert lookup is not None


def cron(request):
    # Get random domain names and DNS lookups in the same range.
    attempts = []
    selector = Selector()
    while True:
        domain_names = selector.fetch_names(Domain, BATCH_SIZE)
        if not domain_names:
            return render_to_response(request, 'dns/cron.html', locals())
        lookup_names = selector.fetch_names(Lookup, BATCH_SIZE)
        domains_all = domain_names[:]
        lookups_all = lookup_names[:]
        selector.truncate_range(domain_names, lookup_names)
        domain_set = set(domain_names)
        lookup_set = set(lookup_names)
        if (domain_set != lookup_set or
            len(attempts) >= 20 or len(domain_set) != BATCH_SIZE):
            break
        attempts.append(selector.name)
        if selector.order == 'ascending':
            selector.name = domain_names[-1]
        elif selector.order == 'descending':
            selector.name = domain_names[0]
    # Create missing lookups.
    timestamp = datetime.now() - timedelta(days=365)
    missing = [Lookup(key_name=name, backwards=name[::-1], timestamp=timestamp)
               for name in domain_names if name not in lookup_set]
    if not on_production_server:
        assert_missing(missing)
    # Delete obsolete lookups.
    obsolete = [db.Key.from_path('dns_lookup', name)
                for name in lookup_names if name not in domain_set]
    if not on_production_server:
        assert_obsolete(obsolete)
    # Perform update, unless using descending key order (needs debugging).
    if selector.position == 'left' and selector.order == 'descending':
        not_really = True
    else:
        db.put(missing)
        db.delete(obsolete)
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'dns/cron.html', locals())


def test(request):
    start_name = random_name()
    query_ascending = Lookup.all(keys_only=True).order('__key__').filter(
        '__key__ >=', db.Key.from_path('dns_lookup', start_name))
    names_ascending = [key.name() for key in query_ascending.fetch(100)]
    query_descending = Lookup.all(keys_only=True).order('-__key__').filter(
        '__key__ <=', db.Key.from_path('dns_lookup', names_ascending[-1]))
    names_descending = [key.name() for key in query_descending.fetch(100)]
    names_descending.reverse()
    ascending = [('black' if name in names_descending else 'red', name)
                 for name in names_ascending]
    descending = [('black' if name in names_ascending else 'red', name)
                  for name in names_descending]
    missing = sum([int(name not in names_ascending)
                   for name in names_descending])
    percent_missing = 100 * missing / len(names_descending)
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'dns/test.html', locals())
