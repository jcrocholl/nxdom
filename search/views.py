from django import forms
from django.http import HttpResponseRedirect
from ragendja.template import render_to_response

from ideas.models import Idea


class SearchForm(forms.Form):
    keyword = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'text span-4 focus'}))
    position = forms.ChoiceField(
        choices=[('left', 'left'), ('right', 'right')],
        widget=forms.RadioSelect(attrs={'class': 'radio'}))
    length = forms.IntegerField(
        initial=-1,
        widget=forms.TextInput(attrs={'class': 'text span-2'}))
    letters = forms.IntegerField(
        initial=0,
        widget=forms.TextInput(attrs={'class': 'text span-2'}))
    digits = forms.IntegerField(
        initial=-5,
        widget=forms.TextInput(attrs={'class': 'text span-2'}))
    dashes = forms.IntegerField(
        initial=-10,
        widget=forms.TextInput(attrs={'class': 'text span-2'}))
    syllables = forms.IntegerField(
        initial=0,
        widget=forms.TextInput(attrs={'class': 'text span-2'}))


def index(request):
    search_form = SearchForm(request.GET or None)
    keyword = request.GET.get('keyword', '')
    position = request.GET.get('position', 'left')
    idea_list = Idea.all()
    if keyword and position == 'left':
        next = keyword[:-1] + chr(ord(keyword[-1]) + 1)
        idea_list.filter('name >=', keyword)
        idea_list.filter('name <', next)
    elif keyword and position == 'right':
        backwards = keyword[::-1]
        next = backwards[:-1] + chr(ord(backwards[-1]) + 1)
        idea_list.filter('backwards >=', backwards)
        idea_list.filter('backwards <', next)
    if search_form.is_valid():
        score_idea_list = []
        for idea in idea_list.fetch(100):
            score = 0
            score += search_form.cleaned_data['length'] * idea.length
            score += search_form.cleaned_data['letters'] * idea.letters
            score += search_form.cleaned_data['digits'] * idea.digits
            score += search_form.cleaned_data['dashes'] * idea.dashes
            score_idea_list.append((score, idea))
        score_idea_list.sort(reverse=True)
    return render_to_response(request, 'search/index.html', locals())
