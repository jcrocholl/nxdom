from django.conf.urls.defaults import *

urlpatterns = patterns('prefixes.views',
    url(r'^$', 'index'),
    url(r'^([a-z0-9-]+)/$', 'detail'),
)