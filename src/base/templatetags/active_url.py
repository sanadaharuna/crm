import re

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def active_url(context, url):
    try:
        # pattern = '^%s$' % reverse(url)
        pattern = reverse(url).split("/")[1]
    except NoReverseMatch:
        pattern = url

    path = context["request"].path
    return "active" if re.search(pattern, path) else ''
