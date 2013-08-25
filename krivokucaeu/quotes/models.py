from django.db import models


class Book(models.Model):
    '''
    Books table db model
    '''
    title = models.CharField(max_length=256)
    extended_title = models.TextField(blank=True)
    amazon_url = models.TextField(max_length=2000, blank=True)
    amazon_is_referal = models.BooleanField(default=True, blank=True)
    wikipedia_url = models.TextField(max_length=2000, blank=True)
    goodreads_url = models.TextField(max_length=2000, blank=True)
    short_description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


class Author(models.Model):
    '''
    Authors table db model
    '''
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    amazon_url = models.TextField(max_length=2000, blank=True)
    amazon_is_referal = models.BooleanField(default=True, blank=True)
    wikipedia_url = models.TextField(max_length=2000, blank=True)
    goodreads_url = models.TextField(max_length=2000, blank=True)
    short_bio = models.TextField(blank=True)
    # Relation towards books
    books = models.ManyToManyField(Book, blank=True)

    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name)


class Quote(models.Model):
    quote_text = models.TextField()
    quote_context = models.TextField(blank=True)
    book = models.ForeignKey(Book)
    date_added = models.DateField()

    def __unicode__(self):
        # On the fly replace potential newlines not to screw up
        # django admin interface.
        return u'%s\u2026' % (self.quote_text[0:128].replace('\n', ' '))
