from django import forms
from django.http import HttpResponseRedirect
from ragendja.template import render_to_response

from ideas.models import Idea


class SearchForm(forms.Form):
    keyword = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'text span-4 focus'}))
    position = forms.ChoiceField(
        choices=[('left', 'left'), ('right', 'right')])


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
    return render_to_response(request, 'search/index.html', locals())
