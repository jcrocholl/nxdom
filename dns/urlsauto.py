from django.conf.urls.defaults import *

urlpatterns = patterns('dns.views',
    url(r'^cron/$', 'cron'),
)
