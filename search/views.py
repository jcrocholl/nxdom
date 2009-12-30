import logging

from google.appengine.ext import db
from google.appengine.api import memcache

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson

from ragendja.template import render_to_response

from domains.models import Domain, MAX_NAME_LENGTH
from dns.models import Lookup, TOP_LEVEL_DOMAINS
from prefixes.utils import increment_prefix

JSON_FETCH_LIMIT = 100 # Domains for each length from 3 to 12.
MEMCACHE_TIMEOUT = 24 * 60 * 60 # 24 hours.
INITIAL = {
    'left': '', 'right': '',
    'len': -1, 'digits': -2, 'dashes': -5,
    'english': 3, 'spanish': 1, 'french': 1, 'german': 1,
    'prefix': 3, 'suffix': 3,
    'com': 10, 'net': 5, 'org': 5, 'biz': 3, 'info': 3,
    }


class SearchForm(forms.Form):
    left = forms.CharField(max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text keyword span-2 focus'}))
    right = forms.CharField(max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text keyword span-2 right'}))
    len = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    digits = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    dashes = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    english = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    spanish = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    french = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    german = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    prefix = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    suffix = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    com = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    net = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    org = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    biz = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))
    info = forms.FloatField(required=False,
        widget=forms.TextInput(attrs={'class': 'text score'}))

    def clean(self):
        data = self.cleaned_data
        for key in data:
            if data[key] is None:
                data[key] = 0.0
        return data


def best_names_of_length(length, position='left', keyword=''):
    query = Domain.all(keys_only=True)
    if len(keyword) <= 5:
        if keyword:
            query.filter('%s%d' % (position, len(keyword)), keyword)
        query.filter('length', length)
        if position == 'left':
            query.order('-english')
        elif position == 'right':
            query.order('-score')
    else:
        query.filter('length', length)
        query.order('__key__')
        keyword_key = db.Key.from_path('domains_domain', keyword)
        query.filter('__key__ >=', keyword_key)
        next_keyword = increment_prefix(keyword)
        next_key = db.Key.from_path('domains_domain', next_keyword)
        query.filter('__key__ <', next_key)
    return [key.name() for key in query.fetch(50)]


def best_names(position='left', keyword=''):
    # Try to get names from memcache, to avoid datastore queries.
    memcache_key = '%s=%s' % (position, keyword)
    names = memcache.get(memcache_key)
    if names:
        logging.debug('filter_domains: memcache hit for %s', memcache_key)
        return names.split()
    # If not found in cache, get names from the datastore.
    names = []
    length = max(3, len(keyword) + 1)
    while len(names) < 300 and length <= 12:
        names.extend(best_names_of_length(length, position, keyword))
        length += 1
    # Cache results in memcache.
    memcache.set(memcache_key, ' '.join(names), MEMCACHE_TIMEOUT)
    return names


def get_domains_with_cache(names):
    # Try to get domains from memcache.
    from_cache = memcache.get_multi(names)
    if from_cache:
        logging.debug('get_domains_with_cache: memcache hit %d/%d domains' %
                      (len(from_cache), len(names)))
    result = []
    for name, values in from_cache.items():
        try:
            result.append(Domain.from_cache(name, values))
        except ValueError:
            from_cache.pop(name)
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
        # Cache results for one hour.
        memcache.set_multi(to_cache, MEMCACHE_TIMEOUT)
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
    if left:
        names = best_names('left', left)
    else:
        names = best_names('right', right)
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
        query.filter('right%d' % len(right), right)
    elif left:
        query.filter('left%d' % len(left), left)
    query.filter('length', length)
    query.order('-score')
    return query.fetch(JSON_FETCH_LIMIT)


def fetch_dns_lookups(domains):
    keys = [db.Key.from_path('dns_lookup', domain.key().name())
            for domain in domains]
    lookups = db.get(keys)
    for domain, lookup in zip(domains, lookups):
        for tld in TOP_LEVEL_DOMAINS:
            value = getattr(lookup, tld) if lookup else None
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
            properties[attr] = int(bool(getattr(domain, attr)))
        result[domain.key().name()] = properties
    return result


def json(request):
    left = request.GET.get('left', '')
    right = request.GET.get('right', '')
    length = int(request.GET.get('length', MAX_NAME_LENGTH))
    memcache_key = 'left=%s,right=%s,length=%d' % (left, right, length)
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
    return HttpResponse(json, mimetype='application/javascript')
