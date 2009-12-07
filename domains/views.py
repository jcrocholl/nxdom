import random
from datetime import datetime

from google.appengine.ext import db
from google.appengine.ext.db import stats

from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from domains.models import MAX_NAME_LENGTH, DOMAIN_CHARS, OBSOLETE_ATTRIBUTES
from domains.models import Domain
from prefixes.selectors import Selector, random_name

BATCH_SIZE_FETCH = 100
BATCH_SIZE_UPDATE = 100


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
    selector = Selector()
    query = selector.select(Domain)
    update_description = selector.description()
    domains = query.fetch(BATCH_SIZE_FETCH)
    count_random = len(domains)
    count_obsolete = 0
    count_languages = 0
    for domain in domains:
        if (len(deleted_domains) >= BATCH_SIZE_UPDATE or
            len(updated_domains) >= BATCH_SIZE_UPDATE):
            break
        if len(domain.key().name()) > MAX_NAME_LENGTH:
            deleted_domains.append(domain)
            continue
        updated = False
        for attr in OBSOLETE_ATTRIBUTES:
            if hasattr(domain, attr):
                delattr(domain, attr)
                updated = True
        if updated:
            count_obsolete += 1
        if domain.language_scores_need_update():
            domain.update_language_scores()
            count_languages += 1
            updated = True
        if (len(domain.key().name()) > 6 and
            domain.english == 0 and domain.spanish == 0 and
            domain.french == 0 and domain.german == 0):
            deleted_domains.append(domain)
            continue
        if updated:
            domain.timestamp = datetime.now()
            updated_domains.append(domain)
    db.put(updated_domains)
    db.delete(deleted_domains)
    count_updated = len(updated_domains)
    count_deleted = len(deleted_domains)
    domain_list = updated_domains[:10] + [None] + deleted_domains[:10]
    refresh_seconds = request.GET.get('refresh', 0)
    return render_to_response(request, 'domains/index.html', locals())


def descending(request):
    start_name = random_name()
    query_ascending = Domain.all(keys_only=True).order('__key__').filter(
        '__key__ >=', db.Key.from_path('domains_domain', start_name))
    names_ascending = [key.name() for key in query_ascending.fetch(100)]
    query_descending = Domain.all(keys_only=True).order('-__key__').filter(
        '__key__ <=', db.Key.from_path('domains_domain', names_ascending[-1]))
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
    return render_to_response(request, 'domains/descending.html', locals())
