from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import quotes.models as qm
import itertools

current_section = 'quote'


def quote_by_id(request, id):
    '''
    Retrieve quote by ID
    '''
    try:
        q = qm.Quote.objects.get(pk=id)
    except qm.Author.DoesNotExist:
        raise Http404
    counter = itertools.count()
    t = get_template('quotes/quote_display.html')
    html = t.render(Context({
        'quote': q,
        'counter': counter,
        'current_section': current_section
    }))
    return HttpResponse(html)
