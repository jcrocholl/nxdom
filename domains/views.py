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
from indexes.models import Comparison

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


def color(result, trunc1, trunc2):
    colored = []
    for name in result:
        if name not in trunc1:
            colored.append('<span style="color:gray">%s</span>' % name)
        elif name not in trunc2:
            colored.append('<span style="color:red">%s</span>' % name)
        else:
            colored.append(name)
    return colored


def descending(request):
    comparison = Comparison(path=request.META.get('PATH_INFO', ''),
                            message="error",
                            timestamp=datetime.now())
    comparison.put()
    start_name = request.GET.get('start', random_name())
    # Build and execute query 1.
    gql1 = ' '.join(("SELECT __key__ FROM domains_domain",
                     "WHERE __key__ >= :1 ORDER BY __key__ ASC",
                     "LIMIT 100"))
    key1 = db.Key.from_path('domains_domain', start_name)
    comparison.gql1 = gql1.replace(':1', repr(key1))
    start_time = time.time()
    keys1 = GqlQuery(gql1, key1).fetch(100)
    comparison.seconds1 = time.time() - start_time
    result1 = [key.name() for key in keys1]
    comparison.result1 = ' '.join(result1)
    # Build and execute query 2.
    gql2 = ' '.join(("SELECT __key__ FROM domains_domain",
                     "WHERE __key__ <= :1 ORDER BY __key__ DESC",
                     "LIMIT 100"))
    key2 = db.Key.from_path('domains_domain', result1[-1])
    comparison.gql2 = gql2.replace(':1', repr(key2))
    start_time = time.time()
    keys1 = GqlQuery(gql2, key2).fetch(100)
    comparison.seconds2 = time.time() - start_time
    result2 = [key.name() for key in keys1]
    comparison.result2 = ' '.join(result2)
    # Check sort order.
    message = []
    if sorted(result1) != result1:
        message.append("query 1 returned incorrect sort order")
    if sorted(result2, reverse=True) != result2:
        message.append("query 2 returned incorrect sort order")
    # Truncate result lists if necessary.
    trunc1 = result1[:]
    trunc2 = result2[:]
    if trunc1 and trunc2 and trunc2[-1] < trunc1[0]:
        while trunc1 and trunc2 and trunc2[-1] < trunc1[0]:
            del trunc2[-1]
    elif trunc1 and trunc2 and trunc1[0] < trunc2[-1]:
        while trunc1 and trunc2 and trunc1[0] < trunc2[-1]:
            del trunc1[0]
    comparison.trunc1 = ' '.join(trunc1)
    comparison.trunc2 = ' '.join(trunc2)
    # Count missing entries.
    set1 = set(trunc1)
    set2 = set(trunc2)
    comparison.missing1 = sum([int(name not in set1) for name in trunc2])
    comparison.missing2 = sum([int(name not in set2) for name in trunc1])
    # Human-readable error message.
    if comparison.missing1:
        message.append("query 1 missed %d items" % comparison.missing1)
    if comparison.missing2:
        message.append("query 2 missed %d items" % comparison.missing2)
    # Save the results.
    comparison.message = ' and '.join(message)
    comparison.put()
    # User-friendly HTML output.
    next_random_name = random_name()
    refresh_seconds = request.GET.get('refresh', 0)
    colored1 = color(result1, trunc1, trunc2)
    colored2 = color(result2, trunc2, trunc1)
    return render_to_response(request, 'domains/descending.html', locals())
