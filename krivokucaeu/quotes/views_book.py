from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import quotes.models as qm

current_section = 'book'


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
        'authors': b.author_set.all(),
        'current_section': current_section
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


def books_all(request):
    '''
    List all the books
    '''
    books_list = {}
    # Sort them by first letter
    books = qm.Book.objects.order_by('title').all()

    for book in books:
        letter = book.first_letter_of_title()
        try:
            books_list[letter]
        except KeyError:
            books_list[letter] = []
        books_list[letter].append(book)

    t = get_template('quotes/books_all.html')
    html = t.render(Context({
        'books': books_list,
        'current_section': current_section
    }))
    return HttpResponse(html)
