import logging
import random

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from names.models import Idea
import counters.utils as counters


class EnterNamesForm(forms.Form):
    names = forms.CharField(
        max_length=10000,
        widget=forms.TextInput(attrs={'class': 'text span-17 focus'}))


class UploadNamesForm(forms.Form):
    upload = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'upload'}))


def index(request):
    # Save newly entered name ideas.
    enter_names_form = EnterNamesForm(
        request.POST if 'submit_names' in request.POST else None)
    if enter_names_form.is_valid():
        names = enter_names_form.cleaned_data['names'].split()
        return create_ideas(request, names)
    # Save new name ideas from file upload.
    upload_names_form = UploadNamesForm(
        request.POST if 'upload_file' in request.POST else None,
        request.FILES if 'upload' in request.FILES else None)
    if 'upload' in request.FILES:
        upload = request.FILES['upload']
        # logging.debug("Content-Length: %d", len(upload['content']))
        # logging.debug("Content-Type: %s", upload['content-type'])
        names = upload.read().split()
        selected = [random.choice(names) for index in range(300)]
        logging.debug(selected[:10])
        return create_ideas(request, selected)
    # Display list of recent names.
    idea_list = Idea.all().order('-created').fetch(20)
    idea_count = counters.get_count('names_idea')
    return render_to_response(request, 'names/index.html', locals())


def detail(request, key_name):
    name = get_object_or_404(Name, key_name=key_name)
    return render_to_response(request, 'names/detail.html', locals())


def create_ideas(request, names):
    counter = 0
    for name in names:
        if '.' in name: # Cut off the top level domain.
            name = name[:name.index('.')]
        idea, created = Idea.get_or_insert_with_flag(key_name=name)
        counter += int(created)
    counters.increment('names_idea', counter)
    return HttpResponseRedirect(request.path)
