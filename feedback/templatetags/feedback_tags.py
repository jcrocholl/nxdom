from django import template
from django.template.loader import render_to_string

from google.appengine.api import datastore_errors

from feedback.models import Feedback, Vote
from feedback.forms import FeedbackForm
from feedback.views import get_already_voted

register = template.Library()


@register.simple_tag
def feedback_form(request):
    page = request.META['PATH_INFO']
    feedback_form = FeedbackForm(initial={'page': page})
    return render_to_string('feedback/form.html', locals())


def render_query(request, query, limit=10):
    feedback_list = []
    for feedback in query.fetch(limit):
        try:
            submitter = feedback.submitter  # Attempt to dereference.
            feedback_list.append(feedback)
        except datastore_errors.Error:
            pass  # Ignore feedback if the submitter doesn't exist.
    already_voted = get_already_voted(request)
    return render_to_string('feedback/messages.html', locals())


@register.simple_tag
def feedback_recently(request, page=None):
    if page is None:
        page = request.META['PATH_INFO']
    query = Feedback.all()
    if page != 'all':
        query.filter('page', page)
    query.order('-submitted')
    return render_query(request, query, 20 if page == 'all' else 10)


@register.simple_tag
def feedback_popular(request, page=None):
    if page is None:
        page = request.META['PATH_INFO']
    feedback_list = []
    query = Feedback.all()
    if page != 'all':
        query.filter('page', page)
    query.order('-points')
    query.order('-submitted')
    return render_query(request, query, 20 if page == 'all' else 10)


@register.filter
def in_list(value, arg):
    return value in arg


@register.filter
def is_equal(value, arg):
    return value == arg
