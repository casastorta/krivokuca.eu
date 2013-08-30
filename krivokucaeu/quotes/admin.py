from django.contrib import admin
from quotes import models as qmodels


class AuthorAdmin(admin.ModelAdmin):
    # Author name
    author_name = lambda au, a: qmodels.Author.__unicode__(a)
    author_name.short_description = 'Author (Last name, first name)'
    # Author bio short variant for table display
    bio = lambda au, a: qmodels.Author.shorten_bio(a)
    bio.short_description = "Short biography"

    list_display = \
        ('author_name', 'first_name', 'last_name', 'bio', 'date_added',)
    ordering = ('last_name', 'first_name',)


class BookAdmin(admin.ModelAdmin):
    # Tie book description short variant for table display
    book_desc = lambda bo, b: qmodels.Book.shorten_description(b)
    book_desc.short_description = "Book description"

    list_display = ('title', 'book_desc', 'date_added',)


class QuoteAdmin(admin.ModelAdmin):
    quote_display = lambda m, q: '%s' % (q)
    list_display = ('quote_display', 'book', 'date_added', )
    list_filter = ('book', 'date_added')
    date_hierarchy = 'date_added'


class ClickAdmin(admin.ModelAdmin):
    # Tie click name with book or author
    link_display = lambda ca, c: \
        qmodels.ClickLog.link_description(c)
    link_display.short_description = "Link destination"
    # Cut of URL if too long
    url_display = lambda ca, c: \
        qmodels.ClickLog.short_url(c)
    url_display.short_description = "Link URL"

    list_display = \
        ('link_display', 'url_display', 'click_type', 'click_destination',
         'click_datetime')
    list_filter = ('click_type', 'click_destination', 'click_datetime',)
    date_hierarchy = 'click_datetime'
    ordering = ('-click_datetime',)


admin.site.register(qmodels.Quote, QuoteAdmin)
admin.site.register(qmodels.Book, BookAdmin)
admin.site.register(qmodels.Author, AuthorAdmin)
admin.site.register(qmodels.ClickLog, ClickAdmin)
