from django.conf.urls.defaults import *

urlpatterns = patterns('domains.views',
    url(r'^$', 'index'),
    url(r'^cron/$', 'cron'),
    url(r'^descending/$', 'descending'),
    url(r'^longest/$', 'longest'),
    url(r'^([a-z0-9-]+)/$', 'detail'),
)
