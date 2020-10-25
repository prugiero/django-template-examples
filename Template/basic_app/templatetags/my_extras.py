from django import template

register = template.Library()
@register.filter(name='cuts')

def cuts(value, arg):
    '''
    cut arg from value ...
    '''

    return value.replace(arg, '')

#register.filter('cut', cut)