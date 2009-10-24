import logging

from django import forms
from django.http import HttpResponseRedirect

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from names.models import Idea


class CreateNamesForm(forms.Form):
    names = forms.CharField(
        max_length=10000,
        widget=forms.TextInput(attrs={'class': 'text span-17 focus'}))


def index(request):
    create_names_form = CreateNamesForm(request.POST or None)
    if create_names_form.is_valid():
        names = create_names_form.cleaned_data['names'].split()
        return create_ideas(request, names)
    idea_count = Idea.all().count()
    idea_list = Idea.all().order('-created').fetch(100)
    return render_to_response(request, 'names/index.html', locals())


def detail(request, key_name):
    name = get_object_or_404(Name, key_name=key_name)
    return render_to_response(request, 'names/detail.html', locals())


def create_ideas(request, names):
    for name in names:
        idea = Idea.get_or_insert(key_name=name)
    return HttpResponseRedirect(request.path)
