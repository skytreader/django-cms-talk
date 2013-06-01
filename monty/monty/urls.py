from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# [CHAD][PRESENTATION POINT]
# Discuss: Why do we need url patterns?
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monty.views.home', name='home'),
    # url(r'^monty/', include('monty.foo.urls')),
    # Enable the admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Sample url pattern for Django CMS. Note the include at the end.
    url(r'^', include('cms.urls')),
)
