from django import template

from marcus import markdown

register = template.Library()

@register.filter(is_safe=True)
def markdown(value):
    return markdown.render(value)
