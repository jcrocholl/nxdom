from django.conf.urls.defaults import *

urlpatterns = patterns('domains.views',
    url(r'^$', 'index'),
    url(r'^cron/([a-z/]*)$', 'cron'),
    url(r'^([a-z0-9-]+)/$', 'detail'),
)
