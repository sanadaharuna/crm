import os
import re

from django import template
from django.urls import NoReverseMatch, reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def active_url(context, url):
    try:
        if os.environ.get("ON_DOCKER"):
            pattern = reverse(url).split("/")[2]
        else:
            pattern = reverse(url).split("/")[1]
    except NoReverseMatch:
        pattern = url

    path = context["request"].path
    return "active" if re.search(pattern, path) else ''
