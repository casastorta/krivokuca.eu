from django.contrib import admin
from quotes import models as qmodels


class QuoteAdmin(admin.ModelAdmin):
    quote_display = lambda m, q: '%s' % (q)
    list_display = ('quote_display', 'book', 'date_added', )
    list_filter = ('book', 'date_added')
    date_hierarchy = 'date_added'


class ClickAdmin(admin.ModelAdmin):
    list_display = ('click_url', 'click_type', 'click_destination')
    list_filter = ('click_type', 'click_destination', 'click_datetime')
    date_hierarchy = 'click_datetime'


admin.site.register(qmodels.Quote, QuoteAdmin)
admin.site.register(qmodels.Book)
admin.site.register(qmodels.Author)
admin.site.register(qmodels.ClickLog, ClickAdmin)
