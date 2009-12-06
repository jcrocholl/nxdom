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
from prefixes.utils import increment_prefix

POPULAR_COUNT = 10 if on_production_server else 1


class PrefixForm(forms.Form):
    prefixes = forms.CharField(
        max_length=200, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-10 focus'}))


def random_prefix(length=2):
    return ''.join([random.choice(DOMAIN_CHARS) for index in range(length)])


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


def update_prefix(prefix):
    field = 'left%d' % len(prefix)
    keys = Domain.all(keys_only=True).order('__key__')
    keys.filter(field, prefix)
    keys = keys.fetch(1000)
    count = len(keys)
    while len(keys) == 1000:
        previous = keys[-1]
        keys = Domain.all(keys_only=True).order('__key__')
        keys.filter(field, prefix).filter('__key__ >', previous)
        keys = keys.fetch(1000)
        count += len(keys)
    prefix = Prefix(key_name=prefix, length=len(prefix),
                    count=count, timestamp=datetime.now())
    prefix.put()
    return prefix


def cron(request):
    names = need_update()
    random.shuffle(names)
    prefix_rows = []
    for name in names[:10]:
        prefix_rows.append([update_prefix(name)])
    return render_to_response(request, 'prefixes/cron.html', locals())


def iterate_dot_com_names(position, chars):
    if position == 'left':
        field = '__key__'
        start = db.Key.from_path('dns_lookup', chars)
        stop = db.Key.from_path('dns_lookup', increment_prefix(chars))
    elif position == 'right':
        field = 'backwards'
        start = chars[::-1]
        stop = increment_prefix(start)
    greater = '>='
    while True:
        query = Lookup.all().order(field)
        query.filter(field + ' ' + greater, start)
        query.filter(field + ' <', stop)
        lookups = query.fetch(1000)
        for lookup in lookups:
            if lookup.com:
                yield lookup.key().name()
        if len(lookups) < 1000:
            break
        if position == 'left':
            start = lookups[-1].key()
        elif position == 'right':
            start = lookups[-1].key().name()[::-1]
        greater = '>'


def count_popular_prefixes(chars, position, names):
    counters = {}
    for name in iterate_dot_com_names(position, chars):
        names.append(name)
        for length in range(3, min(11, len(name) + 1)):
            if position == 'left':
                part = name[:length]
            else:
                part = name[-length:]
            counters[part] = counters.get(part, 0) + 1
    updated = []
    for part in counters:
        count = counters[part]
        if count < POPULAR_COUNT:
            continue
        if position == 'left':
            updated.append(DotComPrefix(key_name=part, length=len(part),
                                        count=count, timestamp=datetime.now()))
        else:
            updated.append(DotComSuffix(key_name=part, length=len(part),
                                        count=count, timestamp=datetime.now()))
    updated.sort(key=lambda prefix: (prefix.length, -prefix.count))
    db.put(updated)
    return updated


def cron_popular(request):
    prefix_rows = []
    suffix_rows = []
    names = []
    while True:
        chars = ''.join([random.choice(DOMAIN_CHARS) for i in range(3)])
        prefixes = count_popular_prefixes(chars, 'left', names)
        if prefixes:
            prefix_rows.append(prefixes)
        suffixes = count_popular_prefixes(chars, 'right', names)
        if suffixes:
            suffix_rows.append(suffixes)
        if len(names) >= 100:
            break
    return render_to_response(request, 'prefixes/cron.html', locals())
