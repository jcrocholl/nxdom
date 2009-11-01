from google.appengine.ext import db

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response

from domains import utils
from domains.models import Domain


class SearchForm(forms.Form):
    keyword = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'text span-4 focus'}))
    position = forms.ChoiceField(
        required=False, choices=[('left', 'left'), ('right', 'right')],
        widget=forms.RadioSelect(attrs={'class': 'radio'}))
    com_expiration = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    net_expiration = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    org_expiration = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    len = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    digits = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    dashes = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))

    def clean(self):
        data = self.cleaned_data
        for key in data:
            if data[key] is None:
                data[key] = self.initial[key]
        return data


def filter_domains(keyword, position):
    domain_list = Domain.all()
    if keyword and position == 'left':
        next = keyword[:-1] + chr(ord(keyword[-1]) + 1)
        domain_list.filter(
            '__key__ >=', db.Key.from_path('domains_domain', keyword))
        domain_list.filter(
            '__key__ <', db.Key.from_path('domains_domain', next))
    elif keyword and position == 'right':
        backwards = keyword[::-1]
        next = backwards[:-1] + chr(ord(backwards[-1]) + 1)
        domain_list.filter('backwards >=', backwards)
        domain_list.filter('backwards <', next)
    return domain_list


def index(request, template_name='search/index.html'):
    search_form = SearchForm(request.GET or None, initial={
            'com_expiration': 50,
            'net_expiration': 30,
            'org_expiration': 20,
            'len': -1,
            'digits': -4,
            'dashes': -8,
            'scowl': 10,
            })
    if search_form.is_valid():
        keyword = search_form.cleaned_data['keyword']
        position = search_form.cleaned_data['position']
        domain_list = filter_domains(keyword, position)
        score_domain_list = score_domains(domain_list.fetch(100),
                                          search_form.cleaned_data)
    return render_to_response(request, template_name, locals())


def score_domains(domain_list, cleaned_data):
    score_domain_list = []
    utils.get_domain_list_whois(domain_list, 'com')
    utils.get_domain_list_whois(domain_list, 'net')
    utils.get_domain_list_whois(domain_list, 'org')
    for domain in domain_list:
        score = 0
        if hasattr(domain, 'com_expiration'):
            score += cleaned_data['com_expiration']
        if hasattr(domain, 'net_expiration'):
            score += cleaned_data['net_expiration']
        if hasattr(domain, 'org_expiration'):
            score += cleaned_data['org_expiration']
        if domain.length is None:
            domain.count_chars()
        score += domain.length * cleaned_data['len']
        score += domain.digits * cleaned_data['digits']
        score += domain.dashes * cleaned_data['dashes']
        domain.check_dictionaries(cleaned_data['keyword'],
                                  cleaned_data['position'])
        score += domain.scowl * cleaned_data['scowl']
        score_domain_list.append((score, domain))
    score_domain_list.sort(
        key=lambda triple: (-triple[0], triple[1].key().name()))
    return score_domain_list[:20]
