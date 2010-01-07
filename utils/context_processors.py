def settings(request):
    from django.conf import settings
    return {'media_version': settings.MEDIA_VERSION}
