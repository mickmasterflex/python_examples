from urllib import urlencode
from hashlib import md5

from django import template

register = template.Library()

@register.simple_tag
def gravatar_for_email(email, size=80):
    return 'http://www.gravatar.com/avatar/{0}?{1}'.format(
            md5(email).hexdigest(),
            urlencode({'size': str(size)}))

