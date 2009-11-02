import random
from datetime import datetime

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response

from domains.models import Domain
from prefixes.models import Prefix

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


class PrefixForm(forms.Form):
    prefixes = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'text span-6 focus'}))


def random_prefix(length=2):
    return ''.join([random.choice(LETTERS) for index in range(length)])


def index(request):
    assert len(LETTERS) == 26
    initial = {'prefixes': ' '.join([random_prefix() for index in range(10)])}
    prefix_form = PrefixForm(request.POST or None, initial=initial)
    if prefix_form.is_valid():
        for prefix in prefix_form.cleaned_data['prefixes'].split():
            update_prefix(prefix)
        return HttpResponseRedirect(request.path)
    matrix = []
    for letter in LETTERS:
        matrix.append((letter, [None] * 26))
    domain_count = 0
    prefix_count = 0
    for prefix in Prefix.all().filter('length', 2):
        x = ord(prefix.key().name()[1]) - ord('a')
        y = ord(prefix.key().name()[0]) - ord('a')
        matrix[y][1][x] = prefix.count
        domain_count += prefix.count
        prefix_count += 1
    domain_estimate = domain_count * 26 * 26 / prefix_count
    letters = LETTERS
    return render_to_response(request, 'prefixes/index.html', locals())


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

