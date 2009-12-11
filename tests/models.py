from google.appengine.ext import db


class Comparison(db.Model):
    path = db.StringProperty()
    params = db.StringProperty()
    message = db.StringProperty()
    timestamp = db.DateTimeProperty()
    # Query 1 and results.
    gql1 = db.StringProperty()
    seconds1 = db.FloatProperty()
    result1 = db.TextProperty()
    trunc1 = db.TextProperty()
    missing1 = db.IntegerProperty()
    # Query 2 and results.
    gql2 = db.StringProperty()
    seconds2 = db.FloatProperty()
    result2 = db.TextProperty()
    trunc2 = db.TextProperty()
    missing2 = db.IntegerProperty()
