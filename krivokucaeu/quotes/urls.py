from django.conf.urls import patterns, url
import quotes.views as qv


urlpatterns = patterns('',
    url(r'^author/(?P<id>\d+)', qv.author_by_id),
    url(r'^author/(?P<slug>[a-z\-]{2,30})', qv.author_by_slug),
    url(r'^book/(?P<id>\d+)', qv.book_by_id),
    url(r'^click/(?P<linksource>[A-Z]{1})/(?P<linktype>[A-Z]{2,4})/'
        '(?P<linkid>\d+)', qv.click),
)
