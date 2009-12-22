import random
import time
from datetime import datetime

from google.appengine.ext import db
from google.appengine.ext.db import stats, GqlQuery

from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from domains.models import MAX_NAME_LENGTH, DOMAIN_CHARS, OBSOLETE_ATTRIBUTES
from domains.models import Domain
from prefixes.selectors import Selector, random_name
from tests.models import Comparison

BATCH_SIZE_FETCH = 50
BATCH_SIZE_UPDATE = 50
BATCH_SIZE_DELETE = 20


def index(request):
    # Display list of recent names.
    newest = Domain.all().order('-timestamp').fetch(10)
    oldest = Domain.all().order('timestamp').fetch(5)
    oldest.reverse()
    domain_list = newest + [''] + oldest
    # Recent statistics.
    domain_stats = stats.KindStat.all().filter('kind_name', 'domains_domain')
    domain_stats = domain_stats.order('-timestamp').fetch(3)
    return render_to_response(request, 'domains/index.html', locals())


def detail(request, key_name):
    name = get_object_or_404(Domain, key_name=key_name)
    return render_to_response(request, 'domains/detail.html', locals())


def cron(request):
    updated_domains = []
    deleted_domains = []
    query = Domain.all().order('timestamp')
    update_description = 'oldest domain names'
    domains = query.fetch(BATCH_SIZE_FETCH)
    count_random = len(domains)
    count_obsolete = 0
    count_languages = 0
    for domain in domains:
        if (len(updated_domains) >= BATCH_SIZE_UPDATE or
            len(deleted_domains) >= BATCH_SIZE_DELETE):
            break
        if len(domain.key().name()) > MAX_NAME_LENGTH:
            deleted_domains.append(domain)
            continue
        domain.before_put()
        if len(domain.key().name()) > 5 and not domain.score:
            deleted_domains.append(domain)
            continue
        updated_domains.append(domain)
    db.put(updated_domains)
    db.delete(deleted_domains)
    count_updated = len(updated_domains)
    count_deleted = len(deleted_domains)
    domain_list = updated_domains[:20] + [None] + deleted_domains[:10]
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'domains/index.html', locals())


def longest(request):
    query = Domain.all(keys_only=True).order('-length')
    query.filter('length > ', MAX_NAME_LENGTH)
    names = [key.name() for key in query.fetch(100)]
    db.delete([db.Key.from_path('domains_domain', name) for name in names])
    db.delete([db.Key.from_path('dns_lookup', name) for name in names])
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'domains/longest.html', locals())


def descending(request):
    start_name = request.GET.get('start', random_name())
    comparison = Comparison(
        message='error', timestamp=datetime.now(),
        path='/domains/descending/', params='start=' + start_name)
    comparison.put()
    comparison.fetch1(
        "SELECT __key__ FROM domains_domain " +
        "WHERE __key__ >= :1 ORDER BY __key__ ASC",
        db.Key.from_path('domains_domain', start_name))
    comparison.fetch2(
        "SELECT __key__ FROM domains_domain " +
        "WHERE __key__ <= :1 ORDER BY __key__ DESC",
        db.Key.from_path('domains_domain', comparison.names1[-1]))
    comparison.check_sort_order()
    comparison.truncate_front_back()
    comparison.count_missing_items()
    comparison.update_and_put()
    next_random_name = random_name()
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'tests/descending.html', locals())
