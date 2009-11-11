import random
from datetime import datetime

from django import forms
from django.http import HttpResponse, HttpResponseRedirect

from google.appengine.ext import db

from ragendja.template import render_to_response
from appenginepatcher import on_production_server

from domains.models import Domain
from prefixes.models import Prefix, Suffix, DotComPrefix, DotComSuffix

LETTERS = 'abcdefghijklmnopqrstuvwxyz-0123456789'
POPULAR_COUNT = 30 if on_production_server else 2


class PrefixForm(forms.Form):
    prefixes = forms.CharField(
        max_length=200, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-10 focus'}))


def random_prefix(length=2):
    return ''.join([random.choice(LETTERS) for index in range(length)])


def index(request):
    size = len(LETTERS)
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
    for letter in LETTERS:
        matrix.append([None] * size)
    domain_count = 0
    prefix_count = 0
    for prefix in Prefix.all().filter('length', 2):
        x = LETTERS.index(prefix.key().name()[1])
        y = LETTERS.index(prefix.key().name()[0])
        matrix[y][x] = prefix.count
        domain_count += prefix.count
        prefix_count += 1
    table_rows = []
    sum_row = [0] * size
    for y, letter in enumerate(LETTERS):
        for x in range(size):
            if matrix[y][x]:
                sum_row[x] += matrix[y][x]
        table_rows.append((letter, matrix[y],
                           sum([count for count in matrix[y] if count])))
    if prefix_count:
        domain_estimate = domain_count * squared / prefix_count
    else:
        domain_estimate = 'unknown'
    letters = LETTERS
    return render_to_response(request, 'prefixes/index.html', locals())


def need_update():
    size = len(LETTERS)
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
    for c1 in LETTERS:
        for c2 in LETTERS:
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


def count_popular_prefixes(domains, position='left'):
    # Lists for batch put and HTML output.
    prefixes = []
    rows = []
    already_counted = set()
    # Update popular prefix and suffix counters.
    for domain in domains:
        name = domain.key().name()
        rows.append([])
        for length in range(3, 7):
            if len(name) < length:
                break
            if position == 'left':
                part = name[:length]
            else:
                part = name[-length:]
            if part in already_counted:
                continue
            already_counted.add(part)
            # Count popular prefixes.
            if position == 'left':
                prefix = DotComPrefix(key_name=part, length=length)
            else:
                prefix = DotComSuffix(key_name=part, length=length)
            prefix.count_domains()
            if prefix.count >= POPULAR_COUNT:
                prefixes.append(prefix)
                rows[-1].append(prefix)
            else:
                prefix.class_extra = ' quiet'
                rows[-1].append(prefix)
                break
        if not rows[-1]:
            rows.pop(-1)
    db.put(prefixes)
    return rows


def cron_popular(request):
    # Pick some random existing .com domain names.
    domains = Domain.all()
    domains.order('com').filter('com !=', None)
    domains.order('-timestamp')
    domains = domains.fetch(20)
    random.shuffle(domains)
    domains = domains[:2]
    # Count popular prefixes and suffixes.
    prefix_rows = count_popular_prefixes(domains, 'left')
    suffix_rows = count_popular_prefixes(domains, 'right')
    return render_to_response(request, 'prefixes/cron.html', locals())
