import mistune

from django import template
from django.conf import settings

register = template.Library()


@register.filter(is_safe=True)
def markdown(value):
    return mistune.markdown(value)
