from django.db import models

# Create your models here.


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
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
