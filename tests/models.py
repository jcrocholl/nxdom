import time
from datetime import datetime

from google.appengine.ext import db
from google.appengine.ext.db import GqlQuery


def replace_args(gql, *args):
    index = 1
    for value in args:
        gql = gql.replace(':%d' % index, repr(value))
        index += 1
    return gql


def color_names(names, not_gray, not_red):
    colored = []
    for name in names:
        if name not in not_gray:
            colored.append('<span style="color:gray">%s</span>' % name)
        elif name not in not_red:
            colored.append('<span style="color:red">%s</span>' % name)
        else:
            colored.append(name)
    return colored


class Comparison(db.Model):
    message = db.StringProperty(default='')
    timestamp = db.DateTimeProperty(required=True)
    path = db.StringProperty(required=True)
    params = db.StringProperty(default='')
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

    def fetch1(self, gql, *args, **kwargs):
        self.messages = []
        limit = kwargs.get('limit', 100)
        start_time = time.time()
        self.keys1 = GqlQuery(gql, *args).fetch(limit)
        self.seconds1 = time.time() - start_time
        self.names1 = [key.name() for key in self.keys1]
        self.gql1 = '%s LIMIT %d' % (replace_args(gql, *args), limit)
        self.result1 = ' '.join(self.names1)

    def fetch2(self, gql, *args, **kwargs):
        limit = kwargs.get('limit', 100)
        start_time = time.time()
        self.keys2 = GqlQuery(gql, *args).fetch(limit)
        self.seconds2 = time.time() - start_time
        self.names2 = [key.name() for key in self.keys2]
        self.gql2 = '%s LIMIT %d' % (replace_args(gql, *args), limit)
        self.result2 = ' '.join(self.names2)

    def check_sort_order(self):
        sorted1 = sorted(self.names1, reverse='DESC' in self.gql1)
        if sorted1 != self.names1:
            self.messages.append(
                "the first query returned incorrect sort order")
        sorted2 = sorted(self.names2, reverse='DESC' in self.gql2)
        if sorted2 != self.names2:
            self.messages.append(
                "the second query returned incorrect sort order")

    def truncate_front_back(self):
        trunc1 = self.names1[:]
        trunc2 = self.names2[:]
        if trunc1 and trunc2 and trunc2[-1] < trunc1[0]:
            while trunc1 and trunc2 and trunc2[-1] < trunc1[0]:
                del trunc2[-1]
        elif trunc1 and trunc2 and trunc1[0] < trunc2[-1]:
            while trunc1 and trunc2 and trunc1[0] < trunc2[-1]:
                del trunc1[0]
        self.set1 = set(trunc1)
        self.set2 = set(trunc2)
        self.trunc1 = ' '.join(trunc1)
        self.trunc2 = ' '.join(trunc2)
        self.colored1 = color_names(self.names1, self.set1, self.set2)
        self.colored2 = color_names(self.names2, self.set2, self.set1)

    def count_missing_items(self):
        self.missing1 = sum([int(name not in self.set1) for name in self.set2])
        self.missing2 = sum([int(name not in self.set2) for name in self.set1])
        if self.missing1:
            self.messages.append(
                "the first query missed %d items" % self.missing1)
        if self.missing2:
            self.messages.append(
                "the second query missed %d items" % self.missing2)

    def update_and_put(self):
        self.message = ' and '.join(self.messages)
        self.timestamp = datetime.now()
        self.put()
