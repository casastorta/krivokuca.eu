from django.http import Http404
from django.shortcuts import redirect
import quotes.models as qm
import datetime


def click(request, linksource, linktype, linkid):
    '''
    Track link
    '''
    model = None
    if linksource == 'B':
        model = qm.Book
    else:
        linksource = 'A'
        model = qm.Author
    try:
        record = model.objects.get(pk=linkid)
    except model.DoesNotExist:
        # No entry (author/book)
        raise Http404
    url = ''
    if linktype == 'AMZN':
        url = record.amazon_url
    elif linktype == 'GR':
        url = record.goodreads_url
    else:
        url = record.wikipedia_url

    if url == '':
        # No link type in db
        raise Http404

    # TODO: Collect user's IP address here

    click = qm.ClickLog(
        click_url=url,
        click_type=linksource,
        click_destination=linktype,
        click_type_destination_id=linkid,
        click_datetime=datetime.datetime.now(),
        click_user_address='127.0.0.1'
    )
    click.save()

    return redirect(url)
