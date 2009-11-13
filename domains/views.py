import random
from datetime import datetime

from google.appengine.ext import db
from google.appengine.ext.db import stats

from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from domains.models import DOMAIN_CHARS, OBSOLETE_ATTRIBUTES
from domains.models import Domain, DnsLookup


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
    name = get_object_or_404(Name, key_name=key_name)
    return render_to_response(request, 'domains/detail.html', locals())


def cron(request):
    updated_domains = []
    random_domains = Domain.all()
    random_key = db.Key.from_path('domains_domain',
        ''.join([random.choice(DOMAIN_CHARS) for i in range(20)]))
    random_domains.filter('__key__ >=', random_key)
    random_domains = random_domains.fetch(100)
    count_obsolete = 0
    count_languages = 0
    for domain in random_domains:
        updated = False
        for attr in OBSOLETE_ATTRIBUTES:
            if hasattr(domain, attr):
                delattr(domain, attr)
                updated = True
        if updated:
            count_obsolete += 1
        if (not hasattr(domain, 'english') or domain.english is None or
            not hasattr(domain, 'spanish') or domain.spanish is None or
            not hasattr(domain, 'french') or domain.french is None or
            not hasattr(domain, 'german') or domain.german is None):
            domain.update_languages()
            count_languages += 1
            updated = True
        if updated:
            domain.timestamp = datetime.now()
            updated_domains.append(domain)
    db.put(updated_domains)
    count_updated = len(updated_domains)
    domain_list = updated_domains[:10]
    return render_to_response(request, 'domains/index.html', locals())
