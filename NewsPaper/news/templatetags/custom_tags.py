from datetime import datetime
from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()

