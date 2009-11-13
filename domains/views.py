import random
from datetime import datetime, date

from google.appengine.ext import db
from google.appengine.ext.db import stats

from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from domains.models import Domain


def index(request):
    # Display list of recent names.
    newest = Domain.all().order('-timestamp').fetch(30)
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


def cron(request, path_rest):
    updates = path_rest.split('/')
    domain_list = Domain.all().order('timestamp').fetch(100)
    for domain in domain_list:
        if 'languages' in updates:
            domain.update_languages()
            domain.timestamp = datetime.now()
    db.put(domain_list)
    domain_list = domain_list[:20]
    return render_to_response(request, 'domains/index.html', locals())
