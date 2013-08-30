from django import template

register = template.Library()


@register.simple_tag
def trackable_link(linkid, linksource, linktype, description):
    '''
    Creates trackable link for tracking through own stat engine
    '''
    track_url = '/q/click/%s/%s/%d' % (linksource, linktype, linkid)
    assembly = '<a href="%s">%s</a>' % \
        (track_url, description)

    return assembly


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
