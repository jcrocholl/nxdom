from google.appengine.ext import db
from google.appengine.api import memcache

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response

from domains.models import Domain

INITIAL = {
    'com': 50, 'net': 30, 'org': 20,
    'len': -1, 'digits': -4, 'dashes': -8,
    'english': 2, 'spanish': 1, 'french': 1, 'german': 1,
    }


class SearchForm(forms.Form):
    left = forms.CharField(
        max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-2 focus'}))
    right = forms.CharField(
        max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-2 right'}))
    com = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    net = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    org = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    len = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    digits = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    dashes = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    english = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    spanish = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    french = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    german = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))

    def clean(self):
        data = self.cleaned_data
        for key in data:
            if data[key] is None:
                data[key] = self.initial[key]
        return data


def filter_domains(keyword, position='left', order='length'):
    # Try to get names from memcache, to avoid datastore queries.
    memcache_key = ','.join((keyword, position, order))
    names = memcache.get(memcache_key)
    if names:
        # logging.debug('memcache hit: %s', memcache_key)
        return names.split()
    # If not found in cache, get names from the datastore.
    domain_list = Domain.all(keys_only=True)
    if 1 <= len(keyword) <= 6:
        domain_list.filter('%s%d' % (position, len(keyword)), keyword)
    elif position == 'left' and len(keyword) > 6:
        domain_list.order('__key__')
        next = keyword[:-1] + chr(ord(keyword[-1]) + 1)
        domain_list.filter(
            '__key__ >=', db.Key.from_path('domains_domain', keyword))
        domain_list.filter(
            '__key__ <', db.Key.from_path('domains_domain', next))
    elif position == 'right' and len(keyword) > 6:
        domain_list.order('backwards')
        backwards = keyword[::-1]
        next = backwards[:-1] + chr(ord(backwards[-1]) + 1)
        domain_list.filter('backwards >=', backwards)
        domain_list.filter('backwards <', next)
    domain_list.order(order)
    names = [key.name() for key in domain_list.fetch(333)]
    # Cache results for 24 hours.
    memcache.set(memcache_key, ' '.join(names), time=24 * 60 * 60)
    return names


def index(request, template_name='search/index.html'):
    search_form = SearchForm(request.GET or INITIAL, initial=INITIAL)
    if search_form.is_valid():
        cleaned_data = search_form.cleaned_data
        left = cleaned_data['left']
        right = cleaned_data['right']
        if len(left) >= len(right):
            position = 'left'
            keyword = left
        else:
            position = 'right'
            keyword = right
        names = set()
        names.update(filter_domains(keyword, position, 'length'))
        if cleaned_data['spanish'] > cleaned_data['english']:
            names.update(filter_domains(keyword, position, '-spanish'))
        elif cleaned_data['french'] > cleaned_data['english']:
            names.update(filter_domains(keyword, position, '-french'))
        elif cleaned_data['german'] > cleaned_data['english']:
            names.update(filter_domains(keyword, position, '-german'))
        else:
            names.update(filter_domains(keyword, position, '-english'))
        if left and position == 'right':
            names = [name for name in names if name.startswith(left)]
        if right and position == 'left':
            names = [name for name in names if name.endswith(right)]
        domain_list = db.get([db.Key.from_path('domains_domain', name)
                              for name in names][:1000])
        domain_list = score_domains(cleaned_data, domain_list)
    return render_to_response(request, template_name, locals())


def score_domains(cleaned_data, domain_list):
    score_domain_list = []
    for domain in domain_list:
        score = 0
        # Available domain names.
        if domain.com is None:
            score += cleaned_data['com']
        if domain.net is None:
            score += cleaned_data['net']
        if domain.org is None:
            score += cleaned_data['org']
        # Character counts.
        if domain.length is None:
            domain.count_chars()
        score += domain.length * cleaned_data['len']
        score += domain.digits * cleaned_data['digits']
        score += domain.dashes * cleaned_data['dashes']
        # Languages.
        if (not hasattr(domain, 'english') or domain.english is None or
            not hasattr(domain, 'spanish') or domain.spanish is None or
            not hasattr(domain, 'french') or domain.french is None or
            not hasattr(domain, 'german') or domain.german is None):
            domain.update_languages()
        score += domain.english * cleaned_data['english']
        score += domain.spanish * cleaned_data['spanish']
        score += domain.french * cleaned_data['french']
        score += domain.german * cleaned_data['german']
        domain.score = score
    domain_list.sort(
        key=lambda domain: (-domain.score, domain.key().name()))
    return domain_list[:50]
