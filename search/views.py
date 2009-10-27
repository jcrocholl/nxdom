from django import forms
from django.http import HttpResponseRedirect
from ragendja.template import render_to_response

from domains.models import Domain


class SearchForm(forms.Form):
    keyword = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'text span-4 focus'}))
    position = forms.ChoiceField(
        required=False, choices=[('left', 'left'), ('right', 'right')],
        widget=forms.RadioSelect(attrs={'class': 'radio'}))
    com_expiration = forms.IntegerField(
        required=False, initial=50,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    net_expiration = forms.IntegerField(
        required=False, initial=30,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    org_expiration = forms.IntegerField(
        required=False, initial=20,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    len = forms.IntegerField(
        required=False, initial=-1,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    digits = forms.IntegerField(
        required=False, initial=-4,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    dashes = forms.IntegerField(
        required=False, initial=-8,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl10 = forms.IntegerField(
        required=False, initial=20,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl20 = forms.IntegerField(
        required=False, initial=15,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl35 = forms.IntegerField(
        required=False, initial=12,
        widget=forms.TextInput(attrs={'class': 'text span-1'}))
    scowl50 = forms.IntegerField(
        required=False, initial=10,
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
        score_domain_list = score_domains(domain_list.fetch(100),
                                          search_form.cleaned_data)
    return render_to_response(request, 'search/index.html', locals())


def ajax(request):
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        keyword = search_form.cleaned_data['keyword'] or ''
        position = search_form.cleaned_data['position'] or 'left'
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
        score_domain_list = score_domains(domain_list.fetch(100),
                                          search_form.cleaned_data)
    else:
        score_domain_list = [(name, search_form[name].errors[0])
                             for name in search_form.errors]
    return render_to_response(request, 'search/tbody.html', locals())


def score_domains(domain_list, cleaned_data):
    score_domain_list = []
    for domain in domain_list:
        score = 0
        if domain.com_expiration:
            score += cleaned_data['com_expiration'] or 50
        if domain.net_expiration:
            score += cleaned_data['net_expiration'] or 30
        if domain.org_expiration:
            score += cleaned_data['org_expiration'] or 20
        domain.count_chars()
        score += domain.len * (cleaned_data['len'] or -1)
        score += domain.digits * (cleaned_data['digits'] or -4)
        score += domain.dashes * (cleaned_data['dashes'] or -8)
        domain.check_dictionaries(cleaned_data['keyword'],
                                  cleaned_data['position'] or 'left')
        if domain.scowl10:
            score += cleaned_data['scowl10'] or 20
        if domain.scowl20:
            score += cleaned_data['scowl20'] or 15
        if domain.scowl35:
            score += cleaned_data['scowl35'] or 12
        if domain.scowl50:
            score += cleaned_data['scowl50'] or 10
        score_domain_list.append((score, domain))
    score_domain_list.sort(
        key=lambda triple: (-triple[0], triple[1].name))
    return score_domain_list[:20]
