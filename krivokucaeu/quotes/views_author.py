from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import quotes.models as qm


def author_by_id(request, id):
    '''
    Retrieve author by ID
    '''
    try:
        a = qm.Author.objects.get(pk=id)
    except qm.Author.DoesNotExist:
        raise Http404
    t = get_template('quotes/author_display.html')
    html = t.render(Context({
        'author': a,
        'books': a.books.all()
    }))
    return HttpResponse(html)


def author_by_slug(request, slug):
    '''
    Retrieve author by slug
    '''
    try:
        a = qm.Author.objects.get(url_slug=slug)
    except qm.Author.DoesNotExist:
        raise Http404
    id = a.id
    return author_by_id(request, id)


def authors_all(request):
    '''
    List all the authors
    '''
    authors_list = {}
    # Sort them by first letter
    authors = qm.Author.objects.order_by('last_name', 'first_name').all()

    for author in authors:
        letter = author.first_letter_of_last_name()
        try:
            authors_list[letter]
        except KeyError:
            authors_list[letter] = []
        authors_list[letter].append(author)

    t = get_template('quotes/authors_all.html')
    html = t.render(Context({
        'authors': authors_list
    }))
    return HttpResponse(html)
