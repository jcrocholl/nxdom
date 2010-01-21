from django.conf.urls.defaults import *

urlpatterns = patterns('search.views',
    url(r'^json/$', 'json'),
    url(r'^cron/$', 'cron'),
    url(r'^vertical/$', 'vertical'),
)
