from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from ragendja.urlsauto import urlpatterns

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = patterns('',
    ('^admin/(.*)', admin.site.root),
    ('^about/$', direct_to_template, {'template': 'about.html'}),
    ('^faq/$', direct_to_template, {'template': 'faq.html'}),
    ('^terms/$', direct_to_template, {'template': 'terms.html'}),
    ('^privacy/$', direct_to_template, {'template': 'privacy.html'}),
    ('^goal/$', direct_to_template, {'template': 'goal.html'}),
    (r'^$', 'search.views.index'),
) + urlpatterns
