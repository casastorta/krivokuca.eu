from django.contrib import sitemaps
import quotes.models as qm


class BookSitemap(sitemaps.Sitemap):
    '''
    Sitemap for Book model
    '''
    changefreq = 'monthly'
    priority = 0.75

    def items(self):
        return qm.Book.objects.all()

    def lastmod(self, obj):
        return obj.date_added


class AuthorSitemap(sitemaps.Sitemap):
    '''
    Sitemap for Author model
    '''
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return qm.Author.objects.all()

    def lastmod(self, obj):
        return obj.date_added


class QuoteSitemap(sitemaps.Sitemap):
    '''
    Sitemap for Quote model
    '''
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return qm.Quote.objects.all()

    def lastmod(self, obj):
        return obj.date_added


class StaticSitemap(sitemaps.Sitemap):
    '''
    Sitemap for "static" pages
    '''
    changefreq = 'monthly'
    priority = 0.4

    pages = {
        'index': '/q/',
        'about': '/q/about/'
    }

    def items(self):
        return self.pages.keys()

    def location(self, obj):
        return self.pages[obj]
