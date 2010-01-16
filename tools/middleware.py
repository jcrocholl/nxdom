from django.http import HttpResponsePermanentRedirect


class DomainRedirectMiddleware(object):

    def process_request(self, request):
        if request.method != 'GET':
            return None
        host = request.get_host()
        if host != 'scoretool.appspot.com':
            return None
        url = '%s://%s%s' % (
            request.is_secure() and 'https' or 'http',
            'www.nxdom.com', request.path)
        if request.META['QUERY_STRING']:
            url += '?' + request.META['QUERY_STRING']
        return HttpResponsePermanentRedirect(url)
