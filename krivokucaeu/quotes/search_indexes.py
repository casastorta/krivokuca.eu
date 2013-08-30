import datetime
from haystack import indexes
from quotes.models import Author, Book, Quote


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title', boost=1.2)
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
    first_name = indexes.CharField(model_attr='first_name', boost=1.1)
    last_name = indexes.CharField(model_attr='last_name', boost=1.1)
    short_bio = indexes.CharField(model_attr='short_bio', boost=0.8)
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
    text = indexes.CharField(document=True, use_template=True, boost=1.5)
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
