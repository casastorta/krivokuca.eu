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
    date_added = models.DateField()

    def __unicode__(self):
        return self.title

    def single_line_description(self):
        short = u'%s' % (self.short_description)
        return short.replace('\n', ' ')

    def shorten_description(self):
        short_description = u'%s\u2026' % \
            (self.single_line_description()[0:96]) \
            if len(self.single_line_description()) > 96 else \
            self.single_line_description()
        return short_description


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
    date_added = models.DateField()
    # Relation towards books
    books = models.ManyToManyField(Book, blank=True)

    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name)

    def single_line_bio(self):
        short = u'%s' % (self.short_bio)
        return short.replace('\n', ' ')

    def shorten_bio(self):
        short_bio = u'%s\u2026' % \
            (self.single_line_bio()[0:96]) \
            if len(self.single_line_bio()) > 96 else \
            self.single_line_bio()
        return short_bio


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
        title = \
            u'%s\u2026' % (self.quote_text[0:128].replace('\n', ' ')) if \
            len(self.quote_text) > 128 else \
            self.quote_text.replace('\n', ' ')
        return title


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

    def link_description(self):
        '''
        Returns description for the link (tie with author or book name)
        '''
        desc = ''
        click_id = self.click_type_destination_id
        click_type = self.click_type
        if click_type == 'A':
            try:
                author = Author.objects.get(pk=click_id)
                desc = u'%s' % (author)
            except:
                desc = "*** Couldn't retrieve author ***"
        elif click_type == 'B':
            try:
                book = Book.objects.get(pk=click_id)
                desc = u'%s' % (book)
            except:
                desc = "*** Couldn't retrieve book ***"
        return desc

    def short_url(self):
        '''
        Shorten URL if needed
        '''
        short_url = u'%s\u2026' % (self.click_url[0:96]) if \
            len(self.click_url) > 96 else self.click_url
        return short_url
