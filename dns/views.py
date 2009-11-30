from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from ragendja.template import render_to_response

from google.appengine.ext import db

from domains.utils import random_prefix
from domains.models import MAX_NAME_LENGTH, Domain
from dns.models import Lookup

BATCH_SIZE = 400


def cron(request):
    # Get 200 random domain names.
    prefix = random_prefix(MAX_NAME_LENGTH)
    query = Domain.all(keys_only=True).order('__key__')
    query.filter('__key__ >=', db.Key.from_path('domains_domain', prefix))
    domain_names = [key.name() for key in query.fetch(BATCH_SIZE)]
    if not domain_names:
        return render_to_response(request, 'dns/cron.html', locals())
    # Get 200 DNS lookups starting from the same random name.
    query = Lookup.all(keys_only=True).order('__key__')
    query.filter('__key__ >=', db.Key.from_path('dns_lookup', prefix))
    lookup_names = [key.name() for key in query.fetch(BATCH_SIZE)]
    # Truncate to the same range if necessary.
    while (domain_names and lookup_names and
           domain_names[-1] > lookup_names[-1]):
        del domain_names[-1]
    while (domain_names and lookup_names and
           lookup_names[-1] > domain_names[-1]):
        del lookup_names[-1]
    domain_set = set(domain_names)
    lookup_set = set(lookup_names)
    # Create missing lookups.
    timestamp = datetime.now() - timedelta(days=7)
    missing = [Lookup(key_name=name, backwards=name[::-1], timestamp=timestamp)
               for name in domain_names if name not in lookup_set]
    db.put(missing)
    # Delete obsolete lookups.
    obsolete = [db.Key.from_path('dns_lookup', name)
                for name in lookup_names if name not in domain_set]
    db.delete(obsolete)
    return render_to_response(request, 'dns/cron.html', locals())
