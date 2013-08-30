import datetime
from haystack import indexes
from quotes.models import Author, Book, Quote


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    object_type = indexes.CharField(model_attr='object_type')
    pub_date = indexes.DateTimeField(model_attr='date_added')

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return \
            self.get_model().objects. \
            filter(date_added__lte=datetime.datetime.now())


class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    object_type = indexes.CharField(model_attr='object_type')
    pub_date = indexes.DateTimeField(model_attr='date_added')

    def get_model(self):
        return Author

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return \
            self.get_model().objects. \
            filter(date_added__lte=datetime.datetime.now())


class QuoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    object_type = indexes.CharField(model_attr='object_type')
    book = indexes.CharField(model_attr='book')
    pub_date = indexes.DateTimeField(model_attr='date_added')

    def get_model(self):
        return Quote

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return \
            self.get_model().objects. \
            filter(date_added__lte=datetime.datetime.now())
