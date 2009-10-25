import logging
import random

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from domains.models import Domain
import counters.utils as counters


class EnterNamesForm(forms.Form):
    names = forms.CharField(
        max_length=10000,
        widget=forms.TextInput(attrs={'class': 'text span-17 focus'}))


class UploadNamesForm(forms.Form):
    upload = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'upload'}))


def index(request):
    # Save newly entered name domains.
    enter_names_form = EnterNamesForm(
        request.POST if 'submit_names' in request.POST else None)
    if enter_names_form.is_valid():
        names = enter_names_form.cleaned_data['names'].split()
        return create_domains(request, names)
    # Save new name domains from file upload.
    upload_names_form = UploadNamesForm(
        request.POST if 'upload_file' in request.POST else None,
        request.FILES if 'upload' in request.FILES else None)
    if 'upload' in request.FILES:
        upload = request.FILES['upload']
        names = upload.read().split()
        random.shuffle(names)
        return create_domains(request, names[:200])
    # Display list of recent names.
    domain_list = Domain.all().order('-created').fetch(20)
    domain_count = counters.get_count('domains_domain')
    return render_to_response(request, 'domains/index.html', locals())


def detail(request, key_name):
    name = get_object_or_404(Name, key_name=key_name)
    return render_to_response(request, 'domains/detail.html', locals())


def create_domains(request, names):
    counter = 0
    for name in names:
        if '.' in name: # Cut off the top level domain.
            name = name[:name.index('.')]
        domain, created = Domain.get_or_insert_with_flag(key_name=name)
        counter += int(created)
    if counter:
        counters.increment('domains_domain', counter)
    return HttpResponseRedirect(request.path)
