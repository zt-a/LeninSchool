from django import template
from main.models import *

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.simple_tag()
def get_name_file(stroka):
    file_name = str(stroka.split('/')[-1])
    return file_name
