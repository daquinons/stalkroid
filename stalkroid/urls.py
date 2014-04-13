from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from stalker.views import AsteroidDetailView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'stalker.views.near', name='near'),
    url(r'^asteroid/(?P<slug>[A-Za-z0-9_\-]+)/$', AsteroidDetailView.as_view( template_name="asteroid.html"), name='asteroid_detail'),
    url(r'^why/$', TemplateView.as_view(template_name = "why.html")),
    url(r'^about/$', TemplateView.as_view(template_name = "about.html")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
