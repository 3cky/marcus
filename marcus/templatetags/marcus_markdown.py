from django import template

from marcus import markdown as md

register = template.Library()

@register.filter(is_safe=True)
def markdown(value):
    return md.render(value)
