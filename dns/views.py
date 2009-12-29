from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from ragendja.template import render_to_response
from appenginepatcher import on_production_server

from google.appengine.ext import db

from domains.utils import random_prefix
from domains.models import MAX_NAME_LENGTH, Domain
from dns.models import Lookup
from prefixes.selectors import Selector, random_name
from tests.models import Comparison

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
            len(attempts) >= 10 or len(domain_set) != BATCH_SIZE):
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


def descending(request):
    start_name = request.GET.get('start', random_name())
    comparison = Comparison(
        message='error', timestamp=datetime.now(),
        path='/dns/descending/', params='start=' + start_name)
    comparison.put()
    comparison.fetch1(
        "SELECT __key__ FROM dns_lookup " +
        "WHERE __key__ >= :1 ORDER BY __key__ ASC",
        db.Key.from_path('dns_lookup', start_name))
    comparison.fetch2(
        "SELECT __key__ FROM dns_lookup " +
        "WHERE __key__ <= :1 ORDER BY __key__ DESC",
        db.Key.from_path('dns_lookup', comparison.names1[-1]))
    comparison.check_sort_order()
    comparison.truncate_front_back()
    comparison.count_missing_items()
    comparison.update_and_put()
    next_random_name = random_name()
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'tests/descending.html', locals())
