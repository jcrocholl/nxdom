from django.conf.urls.defaults import *

urlpatterns = patterns('tests.views',
    url(r'^$', 'index'),
    url(r'^([a-z/]+)/$', 'detail'),
)
