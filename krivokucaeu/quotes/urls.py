from django.conf.urls import patterns, url
from quotes import views as v, views_author as av, views_book as bv, \
    views_quote as qv


urlpatterns = patterns('',
    url(r'^author/(?P<id>\d+)', av.author_by_id),
    url(r'^author/(?P<slug>[a-z\-]{2,30})', av.author_by_slug),

    url(r'authors', av.authors_all),

    url(r'^book/(?P<id>\d+)', bv.book_by_id),
    url(r'^book/(?P<slug>[a-z\-]{2,30})', bv.book_by_slug),

    url(r'books', bv.books_all),

    url(r'quote/(?P<id>\d+)', qv.quote_by_id),

    url(r'^click/(?P<linksource>[A-Z]{1})/(?P<linktype>[A-Z]{2,4})/'
        '(?P<linkid>\d+)', v.click),

    url(r'^about', v.about),
)
