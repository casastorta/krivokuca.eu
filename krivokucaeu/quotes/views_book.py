from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import quotes.models as qm


def book_by_id(request, id):
    '''
    Retrieve book by ID
    '''
    try:
        b = qm.Book.objects.get(pk=id)
    except qm.Book.DoesNotExist:
        raise Http404
    t = get_template('quotes/book_display.html')
    html = t.render(Context({
        'book': b,
        'authors': b.author_set.all()
    }))
    return HttpResponse(html)


def book_by_slug(request, slug):
    '''
    Retrieve book by slug
    '''
    try:
        b = qm.Book.objects.get(url_slug=slug)
    except qm.Book.DoesNotExist:
        raise Http404
    id = b.id
    return book_by_id(request, id)
