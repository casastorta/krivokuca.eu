from django.conf.urls import patterns, url
from quotes import views as qv, views_author as av, views_book as bv


urlpatterns = patterns('',
    url(r'^author/(?P<id>\d+)', av.author_by_id),
    url(r'^author/(?P<slug>[a-z\-]{2,30})', av.author_by_slug),
    url(r'^book/(?P<id>\d+)', bv.book_by_id),
    url(r'^book/(?P<slug>[a-z\-]{2,30})', bv.book_by_slug),
    url(r'^click/(?P<linksource>[A-Z]{1})/(?P<linktype>[A-Z]{2,4})/'
        '(?P<linkid>\d+)', qv.click),
)
