import logging
import random

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from domains.models import Domain
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
    names_form = NamesForm(
        request.POST if 'submit_names' in request.POST else None,
        request.FILES if 'upload' in request.FILES else None)
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
    domain_list = Domain.all().order('-updated').fetch(20)
    domain_count = counters.get_count('domains_domain')
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
        domain, created = Domain.get_or_insert_with_flag(
            key_name=name,
            com_expiration=com_expiration,
            net_expiration=net_expiration,
            org_expiration=org_expiration)
        if created:
            counter += int(created)
        elif (domain.com_expiration != com_expiration or
              domain.net_expiration != net_expiration or
              domain.org_expiration != org_expiration):
            if com_expiration:
                domain.com_expiration = com_expiration
            if net_expiration:
                domain.net_expiration = net_expiration
            if org_expiration:
                domain.org_expiration = org_expiration
            domain.put()
    if counter:
        counters.increment('domains_domain', counter)
    return HttpResponseRedirect(request.path)
