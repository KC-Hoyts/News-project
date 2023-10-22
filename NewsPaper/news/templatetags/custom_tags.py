from datetime import datetime
from django import template
from django.urls import reverse
import locale
from news.models import Post, Comment

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string='%d %B %Y %A %H:%M'):
    if context["LANGUAGE_CODE"] == "ru":
        locale.setlocale(locale.LC_ALL, 'ru')
    elif context["LANGUAGE_CODE"] == "en-us":
        locale.setlocale(locale.LC_TIME, 'en')
    return datetime.utcnow().strftime(format_string)

@register.simple_tag(takes_context=True)
def url_replace(context, ** kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()

@register.simple_tag(takes_context=True)
def previous_post(context, **kwargs):
    all_id = list(Post.objects.all().order_by("date_creation").values("id"))
    for id_id, post_id in enumerate(all_id):
        if context["One_News"].id == post_id["id"] and id_id != 0:
            previous_page_id = all_id[id_id-1]
            context['previous_page'] = previous_page_id["id"]
            return previous_page_id["id"]
        elif context["One_News"].id == post_id["id"] and id_id == 0:
            context['previous_page'] = 0
            return context["One_News"].id


@register.simple_tag(takes_context=True)
def next_post(context, **kwargs):
    all_id = list(Post.objects.all().order_by("date_creation").values("id"))
    for id_id, post_id in enumerate(all_id):
        if context["One_News"].id == post_id["id"] and id_id != len(all_id)-1:
            next_page_id = all_id[id_id + 1]
            context['next_page'] = next_page_id["id"]
            return next_page_id["id"]
        elif context["One_News"].id == post_id["id"] and id_id == len(all_id)-1:
            context['next_page'] = 0
            return context["One_News"].id



