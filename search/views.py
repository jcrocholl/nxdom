from google.appengine.ext import db

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response

from domains.models import Domain


class SearchForm(forms.Form):
    left = forms.CharField(
        max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-2 focus'}))
    right = forms.CharField(
        max_length=40, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-2 right'}))
    com = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    net = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    org = forms.IntegerField(
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


def filter_domains(left, right):
    domain_list = Domain.all()
    if 1 <= len(left) <= 6:
        domain_list.filter('left%d' % len(left), left)
    elif len(left) > 6:
        next = left[:-1] + chr(ord(left[-1]) + 1)
        domain_list.filter(
            '__key__ >=', db.Key.from_path('domains_domain', left))
        domain_list.filter(
            '__key__ <', db.Key.from_path('domains_domain', next))
    if 1 <= len(right) <= 6:
        domain_list.filter('right%d' % len(right), right)
    elif len(right) > 6 and not len(left):
        backwards = right[::-1]
        next = backwards[:-1] + chr(ord(backwards[-1]) + 1)
        domain_list.filter('backwards >=', backwards)
        domain_list.filter('backwards <', next)
    return domain_list


def index(request, template_name='search/index.html'):
    search_form = SearchForm(request.GET or None, initial={
            'com': 50,
            'net': 30,
            'org': 20,
            'len': -1,
            'digits': -4,
            'dashes': -8,
            'scowl': 10,
            })
    if search_form.is_valid():
        domain_list = filter_domains(search_form.cleaned_data['left'],
                                     search_form.cleaned_data['right'])
        domain_list = score_domains(domain_list.fetch(100),
                                    search_form.cleaned_data)
    return render_to_response(request, template_name, locals())


def score_domains(domain_list, cleaned_data):
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
        # Check dictionary words.
        domain.check_dictionaries(cleaned_data['left'], 'left')
        score += domain.scowl * cleaned_data['scowl']
        domain.score = score
    domain_list.sort(
        key=lambda domain: (-domain.score, domain.key().name()))
    return domain_list[:50]
