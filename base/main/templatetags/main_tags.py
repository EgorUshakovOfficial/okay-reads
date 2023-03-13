from django import template

register = template.Library()

def element_at(list, index):
    return list[index]

# Register filters
register.filter('element_at', element_at)