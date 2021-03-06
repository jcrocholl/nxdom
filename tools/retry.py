import logging
import time
import urllib2
import socket

from google.appengine.api import datastore_errors
from google.appengine.runtime import apiproxy_errors

MAX_ATTEMPTS = 10


def retry(func, *args, **kwargs):
    for attempt in range(MAX_ATTEMPTS):
        if attempt:
            seconds = min(300, 2 ** attempt)
            logging.warning(
                "Attempt %d of %d will start in %d seconds." % (
                    attempt + 1, MAX_ATTEMPTS, seconds))
            time.sleep(seconds)
        try:
            return func(*args, **kwargs)
        except (datastore_errors.Timeout, apiproxy_errors.Error,
                urllib2.URLError, socket.error), error:
            logging.error(type(error))
            logging.error(str(error))
            if attempt + 1 >= MAX_ATTEMPTS:
                raise


def retry_objects(func, objects):
    if not objects:
        return
    logging.info("Trying to %s %d objects (%s to %s)" % (
        func.__name__, len(objects),
        objects[0].key().name(), objects[-1].key().name()))
    return retry(func, objects)
