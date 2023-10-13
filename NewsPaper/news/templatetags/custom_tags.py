from datetime import datetime
from django import template
from django.urls import reverse
import locale

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string='%d %B %Y %A %H:%M'):
    if context["LANGUAGE_CODE"] == "ru":
        locale.setlocale(locale.LC_ALL, 'ru')
    elif context["LANGUAGE_CODE"] == "en-us":
        locale.setlocale(locale.LC_TIME, 'en')
    return datetime.utcnow().strftime(format_string)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()

