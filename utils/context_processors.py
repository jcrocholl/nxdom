def settings(request):
    from django.conf import settings
    return {
        'media_version': settings.MEDIA_VERSION,
        'json_version': settings.JSON_VERSION,
        }
