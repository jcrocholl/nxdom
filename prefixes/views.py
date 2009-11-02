import random

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response

from domains.models import Domain
from prefixes.models import Prefix

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


class PrefixForm(forms.Form):
    prefix = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'class': 'text span-2 focus'}))


def index(request):
    prefix_form = PrefixForm(request.POST or None, initial={'prefix':
        ''.join([random.choice(LETTERS) for index in range(3)])})
    if prefix_form.is_valid():
        update_prefix(prefix_form.cleaned_data['prefix'])
        return HttpResponseRedirect(request.path)
    prefix_list = Prefix.all().order('-count').fetch(100)
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
    Prefix(key_name=prefix, length=len(prefix), count=count).put()


def detail(request, prefix):
    if len(prefix) > 6:
        return HttpResponseRedirect('/prefixes/%s/' % prefix[:6])

