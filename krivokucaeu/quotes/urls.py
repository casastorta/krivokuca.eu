from django.views.decorators.cache import cache_page
from django.conf.urls import patterns, url
from haystack.views import SearchView, search_view_factory
from quotes import views as v, views_author as av, views_book as bv, \
    views_quote as qv
from quotes.search_form import QuotesSearchForm
from quotes.sitemaps import BookSitemap, AuthorSitemap, QuoteSitemap, \
    StaticSitemap


sitemaps = {
    'book': BookSitemap,
    'author': AuthorSitemap,
    'quote': QuoteSitemap,
    'pages': StaticSitemap
}

urlpatterns = patterns('',

    url(r'^search/$', cache_page(60 * 3)(search_view_factory(
            view_class=SearchView,
            template='quotes/search.html',
            form_class=QuotesSearchForm,
        ))),

    url(r'^author/(?P<id>\d+)/$', cache_page(60 * 15)(av.author_by_id)),
    url(r'^author/(?P<slug>[a-z\-]{2,30})/$',
        cache_page(60 * 15)(av.author_by_slug)),

    url(r'authors/$', cache_page(60 * 10)(av.authors_all)),

    url(r'^book/(?P<id>\d+)/$', cache_page(60 * 15)(bv.book_by_id)),
    url(r'^book/(?P<slug>[a-z\-]{2,30})/$',
        cache_page(60 * 15)(bv.book_by_slug)),

    url(r'books/$', cache_page(60 * 10)(bv.books_all)),

    url(r'quote/(?P<id>\d+)/$', cache_page(60 * 15)(qv.quote_by_id)),
    # Short caching on the following, but still caching it.
    url(r'quote/$', cache_page(2)(qv.random_quote)),

    url(r'^click/(?P<linksource>[A-Z]{1})/(?P<linktype>[A-Z]{2,4})/'
        '(?P<linkid>\d+)/$', v.click),

    url(r'^about/$', cache_page(60 * 15)(v.about)),

    url(r'^index/$', cache_page(60 * 120)(v.index)),
    url(r'^$', cache_page(60 * 120)(v.index)),

    (r'^sitemap\.xml$',
        ('django.contrib.sitemaps.views.sitemap'),
        {'sitemaps': sitemaps}),
)
