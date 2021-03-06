from django import template
from django.utils import formats
from django.contrib.humanize.templatetags import humanize

register = template.Library()


def get_formatted(value, formater):
    if value:
        naturalday = humanize.naturalday(value)
        localize = formats.localize(value, use_l10n=True)
        if formater:
            dtm = formater.format(localize=localize, naturalday=naturalday)
        else:
            dtm = naturalday
        return localize if naturalday.find(str(value.year)) != -1 else dtm
    return value


@register.filter(is_safe=False)
def naturaldate(value, formater=None):
    if value:
        value = value.date()
    return str(get_formatted(value, formater)).capitalize()
