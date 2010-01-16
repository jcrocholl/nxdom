from django.http import HttpResponsePermanentRedirect


class DomainRedirectMiddleware(object):

    def process_request(self, request):
        if request.method != 'GET':
            # Only redirect GET requests.
            return None
        if request.META['REMOTE_ADDR'] == '0.1.0.1':
            # Don't redirect cron jobs.
            return None
        host = request.get_host()
        if host != 'scoretool.appspot.com':
            # Only redirect default version.
            return None
        url = '%s://%s%s' % (
            request.is_secure() and 'https' or 'http',
            'www.nxdom.com', request.path)
        if request.META['QUERY_STRING']:
            url += '?' + request.META['QUERY_STRING']
        return HttpResponsePermanentRedirect(url)
