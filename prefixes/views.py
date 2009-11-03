import random
from datetime import datetime

from django import forms
from django.http import HttpResponse, HttpResponseRedirect

from ragendja.template import render_to_response

from domains.models import Domain
from prefixes.models import Prefix

LETTERS = 'abcdefghijklmnopqrstuvwxyz-0123456789'


class PrefixForm(forms.Form):
    prefixes = forms.CharField(
        max_length=200, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-6 focus'}))


def random_prefix(length=2):
    return ''.join([random.choice(LETTERS) for index in range(length)])


def index(request):
    size = len(LETTERS)
    random_prefixes = [random_prefix() for index in range(20)]
    initial = {'prefixes': ' '.join(random_prefixes)}
    prefix_form = PrefixForm(request.POST or None, initial=initial)
    if prefix_form.is_valid():
        prefixes = prefix_form.cleaned_data['prefixes'].split()
        if not prefixes:
            prefixes = random_prefixes
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
    squared = size * size
    if prefix_count:
        domain_estimate = domain_count * squared / prefix_count
    else:
        domain_estimate = 'unknown'
    letters = LETTERS
    return render_to_response(request, 'prefixes/index.html', locals())


def cron(request):
    for index in range(20):
        update_prefix(random_prefix())
    return HttpResponse('OK', mimetype="text/plain")


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
    Prefix(
        key_name=prefix,
        length=len(prefix),
        count=count,
        timestamp=datetime.now()).put()


def detail(request, prefix):
    if len(prefix) > 6:
        return HttpResponseRedirect('/prefixes/%s/' % prefix[:6])

