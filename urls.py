from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from django.contrib import admin

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = patterns('',
    ('^admin/(.*)', admin.site.root),
    (r'^$', 'search.views.index'),
) + urlpatterns
