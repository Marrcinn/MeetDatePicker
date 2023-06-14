from django import template

register = template.Library()

@register.filter
def eotw(date):
    return date.weekday() == 0

@register.filter
def django_range(x):
    return range(0,x)

