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
    com_expiration = forms.IntegerField(
        initial=50,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    net_expiration = forms.IntegerField(
        initial=30,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    org_expiration = forms.IntegerField(
        initial=20,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    length = forms.IntegerField(
        initial=-1,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    digits = forms.IntegerField(
        initial=-4,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    dashes = forms.IntegerField(
        initial=-8,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl10 = forms.IntegerField(
        initial=20,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl20 = forms.IntegerField(
        initial=15,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl35 = forms.IntegerField(
        initial=12,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl50 = forms.IntegerField(
        initial=10,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))


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
            if domain.com_expiration:
                score += search_form.cleaned_data['com_expiration']
            if domain.net_expiration:
                score += search_form.cleaned_data['net_expiration']
            if domain.org_expiration:
                score += search_form.cleaned_data['org_expiration']
            domain.count_chars()
            score += search_form.cleaned_data['length'] * domain.length
            score += search_form.cleaned_data['digits'] * domain.digits
            score += search_form.cleaned_data['dashes'] * domain.dashes
            domain.check_dictionaries(keyword, position)
            if domain.scowl10:
                score += search_form.cleaned_data['scowl10']
            if domain.scowl20:
                score += search_form.cleaned_data['scowl20']
            if domain.scowl35:
                score += search_form.cleaned_data['scowl35']
            if domain.scowl50:
                score += search_form.cleaned_data['scowl50']
            score_domain_list.append((score, domain))
        score_domain_list.sort(
            key=lambda triple: (-triple[0], triple[1].name))
        score_domain_list = score_domain_list[:50]
    return render_to_response(request, 'search/index.html', locals())
