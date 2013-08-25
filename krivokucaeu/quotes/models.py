from django.db import models


class Book(models.Model):
    '''
    Books table db model
    '''
    title = models.CharField(max_length=256)
    extended_title = models.TextField(blank=True)
    amazon_url = models.URLField(blank=True)
    amazon_is_referal = models.BooleanField(default=True, blank=True)
    wikipedia_url = models.URLField(blank=True)
    goodreads_url = models.URLField(blank=True)
    short_description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


class Author(models.Model):
    '''
    Authors table db model
    '''
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    amazon_url = models.URLField(blank=True)
    amazon_is_referal = models.BooleanField(default=True, blank=True)
    wikipedia_url = models.URLField(blank=True)
    goodreads_url = models.URLField(blank=True)
    short_bio = models.TextField(blank=True)
    # Relation towards books
    books = models.ManyToManyField(Book, blank=True)

    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name)


class Quote(models.Model):
    '''
    Quotes table db model
    '''
    quote_text = models.TextField()
    quote_context = models.TextField(blank=True)
    date_added = models.DateField()
    # Relation towards books
    book = models.ForeignKey(Book)

    def __unicode__(self):
        # On the fly replace potential newlines not to screw up
        # django admin interface.
        return u'%s\u2026' % (self.quote_text[0:128].replace('\n', ' '))


class ClickLog(models.Model):
    '''
    Outgoing clicks tracking db table model
    '''
    CLICK_TYPES = (
        ('A', 'Author'),
        ('B', 'Book'),
    )
    CLICK_DESTINATIONS = (
        ('GR', 'GoodReads'),
        ('AMZN', 'Amazon'),
        ('WIKI', 'Wikipedia'),
    )
    click_url = models.URLField()
    click_type = models.CharField(max_length=4, choices=CLICK_TYPES)
    click_destination = \
        models.CharField(max_length=4, choices=CLICK_DESTINATIONS)
    click_type_destination_id = models.BigIntegerField()
    click_datetime = models.DateTimeField()
    click_user_address = models.GenericIPAddressField()
