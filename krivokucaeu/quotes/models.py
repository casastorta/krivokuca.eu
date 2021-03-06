from django.db import models
from types import IntType
from django.contrib.sitemaps import ping_google


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
    url_slug = models.SlugField(blank=True)

    def __unicode__(self):
        return self.title

    def single_line_description(self):
        '''
        Converts description to single line (for summaries)
        '''
        short = u'%s' % (self.short_description)
        return short.replace('\n', ' ')

    def shorten_description(self, desired_length=128):
        '''
        Shortens description for summaries.
        '''
        assert type(desired_length) == IntType
        short_description = u'%s\u2026' % \
            (self.single_line_description()[0:desired_length]) \
            if len(self.single_line_description()) > desired_length else \
            self.single_line_description()
        return short_description

    def first_letter_of_title(self):
        '''
        Return first letter of the last name
        '''
        return self.title and self.title[0:1] or ''

    def url_id(self):
        '''
        Returns either url_slug or ID if slug not present
        '''
        return self.url_slug if self.url_slug != '' else self.id

    def get_absolute_url(self):
        '''
        Return absolute URL
        '''
        return '/q/book/%s' % (self.url_id())

    def object_type(self):
        return 'book'

    def save(self, force_insert=False, force_update=False):
        super(Book, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
        # Bare 'except' because we could get a variety
        # of HTTP-related exceptions.
            pass


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
    url_slug = models.SlugField(blank=True)

    # Relation towards books
    books = models.ManyToManyField(Book, blank=True)

    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name)

    def single_line_bio(self):
        '''
        Converts biography to single line (for summaries)
        '''
        short = u'%s' % (self.short_bio)
        return short.replace('\n', ' ')

    def shorten_bio(self, desired_length=128):
        '''
        Shortens biography for summaries.
        '''
        assert type(desired_length) == IntType
        short_bio = u'%s\u2026' % \
            (self.single_line_bio()[0:desired_length]) \
            if len(self.single_line_bio()) > desired_length else \
            self.single_line_bio()
        return short_bio

    def first_letter_of_last_name(self):
        '''
        Return first letter of the last name
        '''
        return self.last_name and self.last_name[0:1] or ''

    def url_id(self):
        '''
        Returns either url_slug or ID if slug not present
        '''
        return self.url_slug if self.url_slug != '' else self.id

    def get_absolute_url(self):
        '''
        Return absolute URL
        '''
        return '/q/author/%s' % (self.url_id())

    def object_type(self):
        return 'author'

    def save(self, force_insert=False, force_update=False):
        super(Author, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
        # Bare 'except' because we could get a variety
        # of HTTP-related exceptions.
            pass


class Quote(models.Model):
    '''
    Quotes table db model
    '''
    quote_text = models.TextField()
    quote_context = models.TextField(blank=True)
    date_added = models.DateField()
    url_slug = models.SlugField(blank=True)

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

    def get_absolute_url(self):
        '''
        Return absolute URL
        '''
        return '/q/quote/%s' % (self.id)

    def object_type(self):
        return 'quote'

    def save(self, force_insert=False, force_update=False):
        super(Quote, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
        # Bare 'except' because we could get a variety
        # of HTTP-related exceptions.
            pass


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
