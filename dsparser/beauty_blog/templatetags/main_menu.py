from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def main_menu():
    menu = Category.objects.all()
    return menu
