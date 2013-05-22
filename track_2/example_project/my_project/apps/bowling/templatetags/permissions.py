from django import template
from django.template import base as template_base

from accounts import constants

register = template.Library()


class IfPermittedNode(template_base.Node):
    child_nodelists = ('nodelist_true', 'nodelist_false')

    def __init__(self, permission_constant, nodelist_true, nodelist_false):
        if not hasattr(constants, permission_constant):
            raise ValueError(
                '{0} must be an accounts constant'.format(permission_constant))
        self.permissions = getattr(constants, permission_constant)
        if not hasattr(self.permissions, '__iter__'):
            self.permissions = [self.permissions]
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false

    def render(self, context):
        if context['user'].profile.is_permitted(self.permissions):
            return self.nodelist_true.render(context)
        else:
            return self.nodelist_false.render(context)


@register.tag
def ifpermitted(parser, token):
    """
    Relies on the inclusion of django.contrib.auth.context_processors.auth
    in the list of settings.TEMPLATE_CONTEXT_PROCESSORS. Needs have access to
    the user in context.

    This is a block tag and expects an endifpermitted tag to close it. To use
    this tag, you will only need to pass one argument. That is the
    accounts.constant name. There is also the 'else' tag you could use, you
    can use to separate the block of True and False responses.

    Example:
    {% ifpermitted PERMISSIONS_ADMIN_ONLY %}
        <h1>I'll allow you to pet my unicorn.</h1>
    {% else %}
        <h1>We don't like your kind around here.</h1>
    {% endifpermitted %}
    """
    try:
        (tag_name, permission_constant) = token.split_contents()
    except ValueError, e:
        raise template.TemplateSyntaxError(
            '{0} takes one argument'.format(token.split_contents()[0]))
    end_tag = 'end{0}'.format(tag_name)
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = template_base.NodeList()
    return IfPermittedNode(permission_constant, nodelist_true, nodelist_false)

