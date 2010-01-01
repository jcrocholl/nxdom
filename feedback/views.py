import logging

from django.http import HttpResponseRedirect
from ragendja.template import render_to_response

from models import Feedback, Vote
from forms import FeedbackForm, VoteForm, DeleteForm


def get_already_voted(request):
    """
    Don't show vote buttons if posted or voted from the same IP.
    """
    ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
    posted = [feedback.id()
              for feedback in Feedback.all(keys_only=True).filter('ip', ip)]
    voted = [vote.feedback_id()
             for vote in Vote.all().filter('ip', ip)]
    # logging.debug('posted=%s voted=%s' % (posted, voted))
    return set(posted + voted)


def index(request):
    """
    Handle post requests or list recent feedback messages.
    """
    # Check if this is a post request with new feedback.
    feedback_form = FeedbackForm(request.POST or None)
    if feedback_form.is_valid():
        return submit(request,
                      page=feedback_form.cleaned_data['page'],
                      message=feedback_form.cleaned_data['message'])
    # Check if this is a post request to vote on a message.
    vote_form = VoteForm(request.POST or None)
    if vote_form.is_valid():
        return vote(request, vote_form.cleaned_data['vote'])
    # Check if this is a post request to delete a message.
    delete_form = DeleteForm(request.POST or None)
    if delete_form.is_valid():
        return delete(request, delete_form.cleaned_data['delete'])
    # Otherwise, display recent feedback.
    feedback_list = Feedback.all()
    feedback_list.order('-points').order('-submitted')
    already_voted = get_already_voted(request)
    return render_to_response(request, 'feedback/index.html', locals())


def submit(request, page, message):
    """
    Save a new feedback message in the database.
    """
    submitter = request.user
    if submitter.is_anonymous():
        submitter = None
    feedback = Feedback(page=page, message=message, submitter=submitter,
                        ip=request.META.get('REMOTE_ADDR', '0.0.0.0'))
    feedback.put()
    return HttpResponseRedirect(page)


def delete(request, id):
    """
    Delete a feedback message if the current user is staff, or it was
    posted from the same IP.
    """
    referer = request.META.get('HTTP_REFERER', '/feedback/')
    redirect = HttpResponseRedirect(referer)
    feedback = Feedback.get_by_id(int(id))
    if feedback is None:
        logging.debug("Feedback '%s' not found." % id)
        return redirect
    if feedback.ip == request.META.get('REMOTE_ADDR', '0.0.0.0'):
        logging.debug("Feedback '%s' deleted by same IP." % id)
        feedback.delete()
    elif request.user.is_staff:
        logging.debug("Feedback '%s' deleted by staff member." % id)
        feedback.delete()
    return redirect


def vote(request, id):
    """
    Add a vote for a feedback message, but not twice from the same IP.
    """
    referer = request.META.get('HTTP_REFERER', '/feedback/')
    redirect = HttpResponseRedirect(referer)
    # Check if the selected feedback exists.
    feedback = Feedback.get_by_id(int(id))
    if feedback is None:
        logging.debug("Feedback '%s' not found." % id)
        return redirect
    # Check if this feedback was posted from the same IP.
    ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
    if feedback.ip == ip:
        logging.debug("Feedback '%s' was posted from the same IP." % id)
        return redirect
    # Check if this IP has already voted for this feedback.
    already = Vote.all().filter('feedback', feedback).filter('ip', ip).count()
    if already:
        logging.debug("Feedback '%s' was already voted %d times from this IP."
                      % (id, already))
        return redirect
    # Register this vote to prevent double voting.
    vote = Vote(feedback=feedback, ip=ip)
    vote.put()
    # Increase the points for this feedback.
    feedback.points += 1
    feedback.put()
    return redirect
