from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from ragendja.template import render_to_response
from appenginepatcher import on_production_server

from google.appengine.ext import db

from domains.utils import random_prefix
from domains.models import MAX_NAME_LENGTH, Domain
from dns.models import Lookup
from prefixes.selectors import Selector, random_name

BATCH_SIZE = 200


def assert_missing(missing):
    keys = [db.Key.from_path('dns_lookup', domain.key().name())
            for domain in missing]
    for lookup in db.get(keys):
        assert lookup is None


def assert_obsolete(obsolete):
    for lookup in db.get(obsolete):
        assert lookup is not None


def cron(request):
    # Get random domain names and DNS loookups in the same range.
    selector = Selector()
    domain_names = selector.fetch_names(Domain, BATCH_SIZE)
    if not domain_names:
        return render_to_response(request, 'dns/cron.html', locals())
    lookup_names = selector.fetch_names(Lookup, BATCH_SIZE)
    domains_all = domain_names[:]
    lookups_all = lookup_names[:]
    selector.truncate_range(domain_names, lookup_names)
    domain_set = set(domain_names)
    lookup_set = set(lookup_names)
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
    name = random_name()
    query_ascending = Lookup.all(keys_only=True).order('__key__').filter(
        '__key__ >=', db.Key.from_path('dns_lookup', name))
    names_ascending = [key.name() for key in query_ascending.fetch(100)]
    query_descending = Lookup.all(keys_only=True).order('-__key__').filter(
        '__key__ <=', db.Key.from_path('dns_lookup', names_ascending[-1]))
    names_descending = [key.name() for key in query_descending.fetch(100)]
    names_descending.reverse()
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'dns/test.html', locals())
