from django import template
register = template.Library()


@register.filter(name='calculateop')
def calculateop(value):
    result = 1 - (value/12)
    return result
