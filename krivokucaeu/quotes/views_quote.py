from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import quotes.models as qm
import itertools
import random

current_section = 'quote'


def quote_by_id(request, id):
    '''
    Retrieve quote by ID
    '''
    try:
        q = qm.Quote.objects.get(pk=id)
    except qm.Quote.DoesNotExist:
        raise Http404
    counter = itertools.count()
    t = get_template('quotes/quote_display.html')
    html = t.render(Context({
        'quote': q,
        'counter': counter,
        'current_section': current_section
    }))
    return HttpResponse(html)


def random_quote(request):
    '''
    Retrieve random quote
    '''
    try:
        # Randomizing in-memory, beware!
        quotes = list(qm.Quote.objects.all())
        random.shuffle(quotes)
    except qm.Quote.DoesNotExist:
        raise Http404
    q = quotes.pop(0)
    del(quotes)
    return quote_by_id(request, q.id)
