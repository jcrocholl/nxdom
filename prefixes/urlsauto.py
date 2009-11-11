from django.conf.urls.defaults import *

urlpatterns = patterns('prefixes.views',
    url(r'^$', 'index'),
    url(r'^cron/$', 'cron'),
    url(r'^cron/popular/$', 'cron_popular'),
)
