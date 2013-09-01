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


def increment_var(parser, token):

    parts = token.split_contents()
    if len(parts) < 2:
        raise template.TemplateSyntaxError(
            "'increment' tag must be of the form: "
            "{% increment <var_name> %}")
    return IncrementVarNode(parts[1])

register.tag('++', increment_var)


class IncrementVarNode(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        try:
            value = context[self.var_name]
            context[self.var_name] = value + 1
            return u""
        except:
            raise template.TemplateSyntaxError("The variable does not exist.")
