from django.conf.urls.defaults import *

urlpatterns = patterns('prefixes.views',
    url(r'^$', 'index'),
    url(r'^cron/$', 'cron'),
    url(r'^cron/suffixes/$', 'cron_suffixes'),
)
