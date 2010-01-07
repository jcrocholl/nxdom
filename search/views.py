import logging
import time
import email.utils

from google.appengine.ext import db
from google.appengine.api import memcache

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.views.decorators.cache import cache_control

from ragendja.template import render_to_response

from domains.models import Domain, MAX_NAME_LENGTH
from dns.models import Lookup, TOP_LEVEL_DOMAINS
from dns.utils import reverse_name
from prefixes.utils import increment_prefix

JSON_FETCH_LIMIT = 60 # Domains for each length from 3 to 12.
MEMCACHE_TIMEOUT = 24 * 60 * 60 # 24 hours.
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


class WeightsForm(forms.Form):
    len = forms.ChoiceField(initial=-3, label="Short names",
        choices=[(1, ''), (0, ''), (-1, ''), (-3, ''), (-9, '')])
    digits = forms.ChoiceField(initial=-2, label="Without numbers",
        choices=[(1, ''), (0, ''), (-1, ''), (-2, ''), (-5, '')])
    dashes = forms.ChoiceField(initial=-5, label="Without dashes",
        choices=[(1, ''), (0, ''), (-1, ''), (-2, ''), (-5, '')])
    english = forms.ChoiceField(initial=3, label="English",
        choices=[(-1, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    spanish = forms.ChoiceField(initial=1, label="Spanish (Espa&ntilde;ol)",
        choices=[(-1, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    french = forms.ChoiceField(initial=1, label="French (Fran&ccedil;ais)",
        choices=[(-1, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    german = forms.ChoiceField(initial=1, label="German (Deutsch)",
        choices=[(-1, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    prefix = forms.ChoiceField(initial=3, label="Popular prefixes",
        choices=[(-1, ''), (0, ''), (1, ''), (3, ''), (9, '')])
    suffix = forms.ChoiceField(initial=3, label="Popular suffixes",
        choices=[(-1, ''), (0, ''), (1, ''), (3, ''), (9, '')])


class RegistrarForm(forms.Form):
    registrar = forms.ChoiceField(choices=REGISTRAR_CHOICES)


def index(request, template_name='search/index.html'):
    search_form = SearchForm(request.GET or None)
    weights_form = WeightsForm(request.GET or None)
    registrar_form = RegistrarForm(request.GET or
                                   {'registrar': 'moniker.com'})
    return render_to_response(request, template_name, locals())


def score_domains(cleaned_data, domain_list):
    score_domain_list = []
    for domain in domain_list:
        score = 0
        # Character counts.
        score += domain.length * cleaned_data['len']
        score += domain.digits * cleaned_data['digits']
        score += domain.dashes * cleaned_data['dashes']
        # Language scores.
        if domain.language_scores_need_update():
            domain.update_language_scores()
        score += domain.english * cleaned_data['english']
        score += domain.spanish * cleaned_data['spanish']
        score += domain.french * cleaned_data['french']
        score += domain.german * cleaned_data['german']
        # Popular prefixes and suffixes.
        if domain.popularity_scores_need_update():
            domain.update_popularity_scores()
        score += domain.prefix * cleaned_data['prefix']
        score += domain.suffix * cleaned_data['suffix']
        # Available domain names.
        for tld in TOP_LEVEL_DOMAINS:
            if hasattr(domain, tld) and getattr(domain, tld) == 0:
                score += cleaned_data[tld]
        domain.weighted_score = score
    domain_list.sort(
        key=lambda domain: (-domain.weighted_score, domain.key().name()))
    return domain_list[:50]


def fetch_candidates(left, right, length):
    query = Domain.all()
    if len(right) > len(left):
        right = right[:6]
        query.filter('right%d' % len(right), right)
    elif left:
        left = left[:6]
        query.filter('left%d' % len(left), left)
    query.filter('length', length)
    query.order('-score')
    return query.fetch(JSON_FETCH_LIMIT)


def fetch_dns_lookups(domains):
    keys = [db.Key.from_path('dns_lookup', domain.key().name())
            for domain in domains]
    lookups = db.get(keys)
    for domain, lookup in zip(domains, lookups):
        if not lookup:
            continue
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
        properties = {}
        for attr in 'digits dashes'.split():
            properties[attr] = getattr(domain, attr)
        for attr in 'english spanish french german prefix suffix'.split():
            properties[attr] = int(getattr(domain, attr) * 1000000)
        for attr in TOP_LEVEL_DOMAINS:
            if hasattr(domain, attr):
                properties[attr] = getattr(domain, attr)
        properties['updated'] = domain.updated.strftime('%Y-%m-%dT%H:%M:%SZ')
        result[domain.key().name()] = properties
    return result


@cache_control(public=True, max_age=MEMCACHE_TIMEOUT)
def json(request):
    left = request.GET.get('left', '')
    right = request.GET.get('right', '')
    length = int(request.GET.get('length', MAX_NAME_LENGTH))
    current_version = 3
    version = int(request.GET.get('version', current_version))
    if version > current_version:
        version = current_version
    memcache_key = 'json%d,%s,%s,%d' % (version, left, right, length)
    json = memcache.get(memcache_key)
    if json:
        logging.debug('json: memcache hit for %s', memcache_key)
    else:
        domains = fetch_candidates(left, right, length)
        fetch_dns_lookups(domains)
        result = domains_to_dict(domains)
        json = simplejson.dumps(result, separators=(',',':'))
        json = json.replace('},', '},\n ')
        memcache.set(memcache_key, json, MEMCACHE_TIMEOUT)
    response = HttpResponse(json, mimetype='application/javascript')
    expires = time.time() + MEMCACHE_TIMEOUT
    response['Expires'] = email.utils.formatdate(expires)[:26] + 'GMT'
    return response
