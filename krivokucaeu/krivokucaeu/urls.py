from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import quotes.urls as qurls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'krivokucaeu.views.home', name='home'),
    # url(r'^krivokucaeu/', include('krivokucaeu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^q/', include(qurls)),
)
