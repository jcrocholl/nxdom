import logging
import random
from datetime import datetime, date

from google.appengine.ext import db
from google.appengine.ext.db import stats

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from domains.models import Domain, Dns, Whois
from domains import utils
import counters.utils as counters


class NamesForm(forms.Form):
    names = forms.CharField(
        label="Enter domain names here", max_length=10000, required=False,
        widget=forms.TextInput(attrs={'class': 'text span-17 focus'}))
    upload = forms.FileField(
        label="Or upload a text file", required=False,
        widget=forms.FileInput(attrs={'class': 'upload'}))
    com_expiration = forms.DateField(
        label="com", required=False,
        widget=forms.DateInput(attrs={'class': 'text span-3'}))
    net_expiration = forms.DateField(
        label="net", required=False,
        widget=forms.DateInput(attrs={'class': 'text span-3'}))
    org_expiration = forms.DateField(
        label="org", required=False,
        widget=forms.DateInput(attrs={'class': 'text span-3'}))


def index(request):
    # Save newly entered name domains.
    names_form = NamesForm(request.POST or None, request.FILES or None)
    if names_form.is_valid():
        names = names_form.cleaned_data['names'].split()
        if 'upload' in request.FILES:
            upload = request.FILES['upload']
            names.extend(upload.read().split())
        random.shuffle(names)
        return create_domains(
            request, names[:200],
            names_form.cleaned_data['com_expiration'],
            names_form.cleaned_data['net_expiration'],
            names_form.cleaned_data['org_expiration'])
    # Display list of recent names.
    domain_list = Domain.all().order('-timestamp').fetch(20)
    utils.get_domain_list_whois(domain_list, 'com')
    utils.get_domain_list_whois(domain_list, 'net')
    utils.get_domain_list_whois(domain_list, 'org')
    domain_count = counters.get_count('domains_domain')
    # Recent statistics.
    domain_stats = stats.KindStat.all().filter('kind_name', 'domains_domain')
    domain_stats = domain_stats.order('-timestamp').fetch(3)
    return render_to_response(request, 'domains/index.html', locals())


def detail(request, key_name):
    name = get_object_or_404(Name, key_name=key_name)
    return render_to_response(request, 'domains/detail.html', locals())


def create_domains(request, names,
                   com_expiration=None,
                   net_expiration=None,
                   org_expiration=None):
    counter = 0
    for name in names:
        if '.' in name: # Cut off the top level domain.
            name = name[:name.index('.')]
        domain, created = Domain.get_or_insert_with_flag(key_name=name)
        if created:
            counter += 1
            if com_expiration:
                Whois(key_name=name + '.com',
                      expiration=com_expiration,
                      timestamp=date.today()).put()
            if net_expiration:
                Whois(key_name=name + '.net',
                      expiration=net_expiration,
                      timestamp=date.today()).put()
            if org_expiration:
                Whois(key_name=name + '.org',
                      expiration=org_expiration,
                      timestamp=date.today()).put()
    if counter:
        counters.increment('domains_domain', counter)
    return HttpResponseRedirect(request.path)
