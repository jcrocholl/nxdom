import logging
import time
import email.utils

from google.appengine.ext import db
from google.appengine.api import memcache

from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.utils import simplejson
from django.views.decorators.cache import cache_control, cache_page

from ragendja.template import render_to_response

from domains.models import Domain, MAX_NAME_LENGTH
from dns.models import Lookup, TOP_LEVEL_DOMAINS
from dns.utils import reverse_name
from prefixes.utils import increment_prefix
from prefixes.selectors import random_prefix

JSON_FETCH_LIMIT = 60  # Domains for each length from 3 to 12.
MEMCACHE_TIMEOUT = 24 * 60 * 60  # 24 hours.
PRIORITY_CHOICES = [
    ('short', "Shortest names first"),
    ('letters', "Without numbers and dashes"),
    ('readable', "More human-readable"),
    ('popular', "Popular beginning or end"),
    ('long', "Longer but most popular"),
    ]
REGISTRAR_CHOICES = [
    ('godaddy.com', 'GoDaddy'),
    ('moniker.com', 'Moniker'),
    ('namecheap.com', 'Namecheap'),
    ('1and1.com', '1&1 (USA)'),
    ('dotster.com', 'Dotster'),
    ]


class SearchForm(forms.Form):
    left = forms.CharField(max_length=40, required=False,
        widget=forms.TextInput(attrs={
                'class': 'text keyword focus',
                'title': "Find names that start with this prefix"}))
    right = forms.CharField(max_length=40, required=False,
        widget=forms.TextInput(attrs={
                'class': 'text keyword right',
                'title': "Find names that end with this suffix"}))


class PriorityForm(forms.Form):
    priority = forms.ChoiceField(initial='short', label="Priority",
        widget=forms.RadioSelect(),
        choices=PRIORITY_CHOICES)


class WeightsForm(forms.Form):
    len = forms.ChoiceField(initial=-3, label="Short names",
        choices=[(3, ''), (0, ''), (-1, ''), (-3, ''), (-9, '')])
    digits = forms.ChoiceField(initial=-3, label="Without numbers",
        choices=[(3, ''), (0, ''), (-1, ''), (-3, ''), (-9, '')])
    dashes = forms.ChoiceField(initial=-9, label="Without dashes",
        choices=[(3, ''), (0, ''), (-1, ''), (-3, ''), (-9, '')])
    english = forms.ChoiceField(initial=3, label="English",
        choices=[(-3, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    spanish = forms.ChoiceField(initial=1, label="Spanish",
        choices=[(-3, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    french = forms.ChoiceField(initial=1, label="French",
        choices=[(-3, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    german = forms.ChoiceField(initial=1, label="German",
        choices=[(-3, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    prefix = forms.ChoiceField(initial=9, label="Popular prefixes",
        choices=[(-3, ''), (0, ''), (3, ''), (9, ''), (27, '')])
    suffix = forms.ChoiceField(initial=9, label="Popular suffixes",
        choices=[(-3, ''), (0, ''), (3, ''), (9, ''), (27, '')])


class RegistrarForm(forms.Form):
    registrar = forms.ChoiceField(choices=REGISTRAR_CHOICES)


@cache_control(public=True, max_age=MEMCACHE_TIMEOUT)
# @cache_page(5 * 60) # Server side cache for 5 minutes.
def index(request):
    logging.info("Generating home page")
    search_form = SearchForm(request.GET or None)
    priority_form = PriorityForm(request.GET or {'priority': 'popular'})
    weights_form = WeightsForm(request.GET or None)
    registrar_form = RegistrarForm(request.GET or {'registrar': 'godaddy.com'})
    return render_to_response(request, 'search/index.html', locals())


def best_left_right(left, right):
    if left and not right:
        left = left[:6]
    elif right and not left:
        right = right[-6:]
    elif len(left) >= len(right) > 0:
        left = left[:4]
        if len(left) + len(right) > 5:
            right = right[len(left) - 5:]
    elif len(right) > len(left) > 0:
        right = right[-4:]
        if len(left) + len(right) > 5:
            left = left[:5 - len(right)]
    return left, right


def fetch_candidates(left, right, length):
    query = Domain.all()
    if left:
        query.filter('left%d' % len(left), left)
    if right:
        query.filter('right%d' % len(right), right)
    query.filter('length', length)
    query.order('-score')
    return query.fetch(JSON_FETCH_LIMIT)


def update_scores(domains):
    from prefixes.popular import prefix_score, suffix_score
    for domain in domains:
        name = domain.key().name()
        domain.prefix, domain._best_prefix = prefix_score(name)
        domain.suffix, domain._best_suffix = suffix_score(name)
        domain.update_score()


def fetch_dns_lookups(domains):
    keys = [db.Key.from_path('dns_lookup', domain.key().name())
            for domain in domains]
    lookups = db.get(keys)
    for index in range(len(domains) - 1, -1, -1):
        lookup = lookups[index]
        if not lookup:
            domains.pop(index)
            continue
        domain = domains[index]
        domain.updated = lookup.timestamp
        for tld in TOP_LEVEL_DOMAINS:
            value = getattr(lookup, tld, None)
            if isinstance(value, basestring):
                value = reverse_name(value)
            if value:
                setattr(domain, tld, value)


def domains_to_dict(domains):
    result = {}
    for domain in domains:
        if hasattr(domain, 'com') and domain.com:
            continue
        properties = {}
        for attr in 'digits dashes'.split():
            properties[attr] = getattr(domain, attr)
        for attr in 'english spanish french german prefix suffix'.split():
            properties[attr] = int(getattr(domain, attr) * 1000000)
        for attr in TOP_LEVEL_DOMAINS:
            if hasattr(domain, attr):
                properties[attr] = getattr(domain, attr)
        if hasattr(domain, '_best_prefix'):
            properties['pl'] = len(domain._best_prefix)
        if hasattr(domain, '_best_suffix'):
            properties['sl'] = len(domain._best_suffix)
        properties['updated'] = domain.updated.strftime('%Y-%m-%dT%H:%M:%SZ')
        result[domain.key().name()] = properties
    return result


def generate_json(left, right, length):
    domains = fetch_candidates(left, right, length)
    update_scores(domains)
    fetch_dns_lookups(domains)
    result = domains_to_dict(domains)
    json = simplejson.dumps(result, separators=(',', ':'))
    json = json.replace('},', '},\n ')
    return json


@cache_control(public=True, max_age=MEMCACHE_TIMEOUT)
def json(request):
    left, right = best_left_right(request.GET.get('left', ''),
                                  request.GET.get('right', ''))
    length = int(request.GET.get('length', 8))
    version = int(request.GET.get('version', settings.JSON_VERSION))
    version = min(version, settings.JSON_VERSION)
    memcache_key = 'json%d,%s,%s,%d' % (version, left, right, length)
    json = memcache.get(memcache_key)
    if json is None:
        json = generate_json(left, right, length)
        memcache.set(memcache_key, json, MEMCACHE_TIMEOUT)
        logging.info("Generated JSON for %s", memcache_key)
    else:
        logging.info("Found cached JSON for %s", memcache_key)
    response = HttpResponse(json, mimetype='application/javascript')
    expires = time.time() + MEMCACHE_TIMEOUT
    response['Expires'] = email.utils.formatdate(expires)[:26] + 'GMT'
    return response


def cron(request):
    """
    Preload memcache with some JSON requests.
    """
    version = settings.JSON_VERSION
    left = random_prefix(length_choices=[1, 2, 3])
    right = ''
    lines = []
    for length in range(max(2, len(left)) + 1, MAX_NAME_LENGTH + 1):
        memcache_key = 'json%d,%s,%s,%d' % (version, left, right, length)
        json = generate_json(left, right, length)
        memcache.set(memcache_key, json, MEMCACHE_TIMEOUT)
        lines.append(json[:120] + '...' if len(json) > 120 else json)
    return render_to_response(request, 'search/cron.html', locals())


def vertical(request):
    headers = 'Negative Neutral Positive Important Critical'.split()
    return render_to_response(request, 'search/vertical.html', locals())
