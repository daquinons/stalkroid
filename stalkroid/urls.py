from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','stalker.views.near', name='near'),
    # Examples:
    # url(r'^$', 'stalkroid.views.home', name='home'),
    # url(r'^stalkroid/', include('stalkroid.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
