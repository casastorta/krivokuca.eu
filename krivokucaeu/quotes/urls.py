from django.conf.urls import patterns, url
import quotes.views as qv


urlpatterns = patterns('',
    url(r'^author/(?P<id>\d+)', qv.author_by_id),
    url(r'^click/(?P<linksource>[A-Z]{1})/(?P<linktype>[A-Z]{2,4})/'
        '(?P<linkid>\d+)', qv.click),
)
