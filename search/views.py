import logging

from google.appengine.ext import db
from google.appengine.api import memcache

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response

from domains.models import Domain
from dns.models import Lookup, TOP_LEVEL_DOMAINS
from prefixes.utils import increment_prefix

INITIAL = {
    'left': '', 'right': '',
    'len': -1, 'digits': -4, 'dashes': -8,
    'english': 2, 'spanish': 1, 'french': 1, 'german': 1,
    'com': 50, 'net': 30, 'org': 20, 'biz': 20, 'info': 20,
    }


class SearchForm(forms.Form):
    left = forms.CharField(
        max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-2 focus'}))
    right = forms.CharField(
        max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-2 right'}))
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
    com = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    net = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    org = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    biz = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    info = forms.FloatField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))

    def clean(self):
        data = self.cleaned_data
        for key in data:
            if data[key] is None:
                data[key] = self.initial[key]
        return data


def filter_domains(left, right, order='length'):
    # Try to get names from memcache, to avoid datastore queries.
    memcache_key = ','.join((left, right, order))
    names = memcache.get(memcache_key)
    if names:
        logging.debug('filter_domains: memcache hit for %s', memcache_key)
        return names.split()
    # If not found in cache, get names from the datastore.
    domain_list = Domain.all(keys_only=True)
    if 1 <= len(left) <= 6:
        domain_list.filter('left%d' % len(left), left)
    elif len(left) > 6:
        domain_list.order('__key__')
        next = increment_prefix(left)
        domain_list.filter(
            '__key__ >=', db.Key.from_path('domains_domain', keyword))
        domain_list.filter(
            '__key__ <', db.Key.from_path('domains_domain', next))
    if 1 <= len(right) <=6:
        domain_list.filter('right%d' % len(right), right)
    elif len(right) > 6:
        domain_list.order('backwards')
        backwards = keyword[::-1]
        next = increment_prefix(backwards)
        domain_list.filter('backwards >=', backwards)
        domain_list.filter('backwards <', next)
    domain_list.order(order)
    names = [key.name() for key in domain_list.fetch(50)]
    # Cache results for 24 hours.
    memcache.set(memcache_key, ' '.join(names), time=24 * 60 * 60)
    return names


def get_domains_with_cache(names):
    # Try to get domains from memcache.
    from_cache = memcache.get_multi(names)
    if from_cache:
        logging.debug('get_domains_with_cache: memcache hit %d/%d domains' %
                      (len(from_cache), len(names)))
    result = [Domain.from_cache(name, from_cache[name])
              for name in from_cache]
    # Fetch missing domains from datastore.
    missing = [name for name in names if name not in from_cache]
    if missing:
        datastore_domains = db.get([db.Key.from_path('domains_domain', name)
                                    for name in missing])
        datastore_lookups = db.get([db.Key.from_path('dns_lookup', name)
                                    for name in missing])
        # Pull DNS results into the Domain instances.
        to_cache = {}
        for domain, lookup in zip(datastore_domains, datastore_lookups):
            if domain is not None:
                for tld in TOP_LEVEL_DOMAINS:
                    value = getattr(lookup, tld) if lookup else None
                    setattr(domain, tld, value)
                result.append(domain)
                to_cache[domain.key().name()] = domain.to_cache()
        # Cache results for 24 hours.
        memcache.set_multi(to_cache, 24 * 60 * 60)
    return result


def index(request, template_name='search/index.html'):
    search_form = SearchForm(request.GET or None, initial=INITIAL)
    if search_form.is_valid():
        cleaned_data = search_form.cleaned_data
    else:
        cleaned_data = INITIAL
    left = cleaned_data['left']
    right = cleaned_data['right']
    if left and right:
        if len(left) >= len(right):
            right = ''
        else:
            left = ''
    names = set()
    names.update(filter_domains(left, right, 'length'))
    if cleaned_data['spanish'] > cleaned_data['english']:
        names.update(filter_domains(left, right, '-spanish'))
    elif cleaned_data['french'] > cleaned_data['english']:
        names.update(filter_domains(left, right, '-french'))
    elif cleaned_data['german'] > cleaned_data['english']:
        names.update(filter_domains(left, right, '-german'))
    else:
        names.update(filter_domains(left, right, '-english'))
    if cleaned_data['left'] and not left:
        left = cleaned_data['left']
        names = [name for name in names if name.startswith(left)]
    if cleaned_data['right'] and not right:
        right = cleaned_data['right']
        names = [name for name in names if name.endswith(right)]
    domain_list = get_domains_with_cache(names)
    domain_list = score_domains(cleaned_data, domain_list)
    return render_to_response(request, template_name, locals())


def score_domains(cleaned_data, domain_list):
    score_domain_list = []
    for domain in domain_list:
        score = 0
        # Available domain names.
        for tld in TOP_LEVEL_DOMAINS:
            if getattr(domain, tld) == False:
                score += cleaned_data[tld]
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
