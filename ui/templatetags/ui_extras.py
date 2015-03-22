import json

from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter
def JSON(obj):
    return mark_safe(json.dumps(obj))
