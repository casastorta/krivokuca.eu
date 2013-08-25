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
    return HttpResponse('<h1>%s</h1>' % (a))
