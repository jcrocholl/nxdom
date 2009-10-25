from django import forms
from django.http import HttpResponseRedirect
from ragendja.template import render_to_response

from domains.models import Domain


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
    domain_list = Domain.all()
    if keyword and position == 'left':
        next = keyword[:-1] + chr(ord(keyword[-1]) + 1)
        domain_list.filter('name >=', keyword)
        domain_list.filter('name <', next)
    elif keyword and position == 'right':
        backwards = keyword[::-1]
        next = backwards[:-1] + chr(ord(backwards[-1]) + 1)
        domain_list.filter('backwards >=', backwards)
        domain_list.filter('backwards <', next)
    if search_form.is_valid():
        score_domain_list = []
        for domain in domain_list.fetch(100):
            score = 0
            score += search_form.cleaned_data['length'] * domain.length
            score += search_form.cleaned_data['letters'] * domain.letters
            score += search_form.cleaned_data['digits'] * domain.digits
            score += search_form.cleaned_data['dashes'] * domain.dashes
            score_domain_list.append((score, domain))
        score_domain_list.sort(reverse=True)
    return render_to_response(request, 'search/index.html', locals())
