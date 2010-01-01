from google.appengine.ext import db

from django.contrib.auth.models import User


class Feedback(db.Model):
    page = db.StringProperty(required=True)
    message = db.StringProperty(required=True)
    points = db.IntegerProperty(default=1)
    ip = db.StringProperty()
    submitter = db.ReferenceProperty(User)
    submitted = db.DateTimeProperty(auto_now_add=True)

    def __unicode__(self):
        return self.message[:50]


class Vote(db.Model):
    feedback = db.ReferenceProperty(Feedback, required=True)
    ip = db.StringProperty(required=True)

    def feedback_id(self):
        return Vote.feedback.get_value_for_datastore(self).id()
