from django.conf.urls.defaults import *

urlpatterns = patterns('search.views',
    url(r'^ajax/$', 'index', {'template_name': 'search/tbody.html'}),
)
