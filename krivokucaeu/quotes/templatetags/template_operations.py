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


@register.simple_tag
def template_exists(template_name):
    try:
        t = template.loader.render_to_string(template_name)
        return t
    except template.TemplateDoesNotExist:
        return ''


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
