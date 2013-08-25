from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import quotes.models as qm


def author_by_id(request, id=1):
    '''
    Retrieve author by ID
    '''
    try:
        a = qm.Author.objects.get(pk=id)
    except qm.Author.DoesNotExist:
        raise Http404
    t = get_template('quotes/author_display.html')
    html = t.render(Context(
        {'author': a}
    ))
    return HttpResponse(html)
