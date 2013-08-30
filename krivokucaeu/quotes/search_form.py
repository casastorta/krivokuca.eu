from haystack.forms import HighlightedSearchForm
from django import forms


class QuotesSearchForm(HighlightedSearchForm):
    '''
    Quotes app search form
    '''

    def __init__(self, arg, **kwargs):
        HighlightedSearchForm.__init__(self, arg, kwargs)
        #self.auto_id = False
        for f in self.fields:
            if isinstance(self.fields[f], forms.CharField) is True:
                self.fields[f].widget.attrs["class"] = "form-control"
                self.fields[f].widget.attrs['placeholder'] = \
                    "Search for author, book or part of the quote"
                self.fields[f].label = ''
                self.fields[f].help_text = ''
