import logging
import random
from datetime import datetime

from django import forms
from django.http import HttpResponse, HttpResponseRedirect

from google.appengine.ext import db

from ragendja.template import render_to_response
from appenginepatcher import on_production_server

from domains.models import Domain, DOMAIN_CHARS
from dns.models import Lookup
from prefixes.models import Prefix, Suffix, DotComPrefix, DotComSuffix
from prefixes.utils import increment_prefix, random_prefix
from tools.retry import retry

BATCH_SIZE = 1000
POPULAR_COUNT = 10 if on_production_server else 1


class PrefixForm(forms.Form):
    prefixes = forms.CharField(
        max_length=200, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-10 focus'}))


def index(request):
    size = len(DOMAIN_CHARS)
    squared = size * size
    names = need_update()
    random.shuffle(names)
    names = names[:20]
    initial = {'prefixes': ' '.join(names)}
    prefix_form = PrefixForm(request.POST or None, initial=initial)
    if prefix_form.is_valid():
        prefixes = prefix_form.cleaned_data['prefixes'].split()
        if not prefixes:
            prefixes = names
        for prefix in prefixes:
            update_prefix(prefix)
        return HttpResponseRedirect(request.path)
    matrix = []
    for letter in DOMAIN_CHARS:
        matrix.append([None] * size)
    domain_count = 0
    prefix_count = 0
    for prefix in Prefix.all().filter('length', 2):
        x = DOMAIN_CHARS.index(prefix.key().name()[1])
        y = DOMAIN_CHARS.index(prefix.key().name()[0])
        matrix[y][x] = prefix.count
        domain_count += prefix.count
        prefix_count += 1
    table_rows = []
    sum_row = [0] * size
    for y, letter in enumerate(DOMAIN_CHARS):
        for x in range(size):
            if matrix[y][x]:
                sum_row[x] += matrix[y][x]
        table_rows.append((letter, matrix[y],
                           sum([count for count in matrix[y] if count])))
    if prefix_count:
        domain_estimate = domain_count * squared / prefix_count
    else:
        domain_estimate = 'unknown'
    letters = DOMAIN_CHARS
    return render_to_response(request, 'prefixes/index.html', locals())


def need_update():
    size = len(DOMAIN_CHARS)
    squared = size * size
    keys = (Prefix.all(keys_only=True).filter('length', 2)
            .order('__key__').fetch(1000))
    if len(keys) == 1000:
        keys.extend(Prefix.all(keys_only=True).filter('length', 2)
                    .filter('__key__ >', keys[-1]).fetch(1000))
    if len(keys) == squared:
        oldest = (Prefix.all(keys_only=True).filter('length', 2)
                  .order('timestamp').fetch(100))
        return [key.name() for key in oldest]
    existing = set([key.name() for key in keys])
    result = []
    for c1 in DOMAIN_CHARS:
        for c2 in DOMAIN_CHARS:
            name = c1 + c2
            if name not in existing:
                result.append(name)
    return result


def count(chars, resume, lookups, Model, cut_prefix):
    counters = {}
    com_counters = {}
    if resume:
        incomplete = Model.all().filter('resume', resume).fetch(20)
        for prefix in incomplete:
            counters[prefix.key().name()] = prefix.count
            com_counters[prefix.key().name()] = prefix.com
    for lookup in lookups:
        name = lookup.key().name()
        for length in range(len(chars), min(12, len(name)) + 1):
            prefix = cut_prefix(name, length)
            counters[prefix] = counters.get(prefix, 0) + 1
            if hasattr(lookup, 'com') and '.' in lookup.com:
                com_counters[prefix] = com_counters.get(prefix, 0) + 1
    resume = False
    if len(lookups) == BATCH_SIZE:
        resume = lookups[-1].key().name()
    timestamp = datetime.now()
    prefixes = []
    for name in counters:
        length = len(name)
        count = counters.get(name, 0)
        com = com_counters.get(name, 0)
        if length > 2 and com < POPULAR_COUNT:
            if not resume or name != cut_prefix(resume, len(name)):
                continue
        prefix = Model(key_name=name, length=length, timestamp=timestamp,
                       count=count, com=com, percentage=100.0 * com / count)
        if resume and name == cut_prefix(resume, len(name)):
            # This counter is incomplete, continue later.
            prefix.resume = resume
        prefixes.append(prefix)
    db.put(prefixes)
    prefixes.sort(key=lambda lookup: (-lookup.count, lookup.key().name()))
    return prefixes


def cron(request):
    refresh_seconds = request.GET.get('refresh', 0)
    prefix = request.GET.get('prefix', random_prefix(2))
    resume = False
    greater = '>='
    start = db.Key.from_path('dns_lookup', prefix)
    stop = db.Key.from_path('dns_lookup', increment_prefix(prefix))
    previous = Prefix.get_by_key_name(prefix)
    if previous and hasattr(previous, 'resume'):
        resume = previous.resume
        logging.info("resuming prefix %s count from %s", prefix, resume)
        greater = '>'
        start = db.Key.from_path('dns_lookup', previous.resume)
    query = Lookup.all().order('__key__')
    query.filter('__key__ ' + greater, start)
    query.filter('__key__ <', stop)
    lookups = retry(query.fetch, BATCH_SIZE)
    prefixes = count(prefix, resume, lookups, Prefix,
                     lambda name, length: name[:length])
    return render_to_response(request, 'prefixes/cron.html', locals())


def cron_suffixes(request):
    refresh_seconds = request.GET.get('refresh', 0)
    suffix = request.GET.get('suffix', random_prefix(2))
    resume = False
    greater = '>='
    start = suffix[::-1]
    stop = increment_prefix(start)
    previous = Suffix.get_by_key_name(suffix)
    if previous and hasattr(previous, 'resume'):
        resume = previous.resume
        logging.info("resuming suffix %s count from %s", suffix, resume)
        greater = '>'
        start = previous.resume[::-1]
    query = Lookup.all().order('backwards')
    query.filter('backwards ' + greater, start)
    query.filter('backwards <', stop)
    lookups = retry(query.fetch, BATCH_SIZE)
    suffixes = count(suffix, resume, lookups, Suffix,
                     lambda name, length: name[-length:])
    return render_to_response(request, 'prefixes/cron.html', locals())
