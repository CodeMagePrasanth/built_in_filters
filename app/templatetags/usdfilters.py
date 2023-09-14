from django import template

register = template.Library()

def swap(value):
    return value.swap()

register.filter('swap',swap) 

# def count(value):
#     return value.count()
# register.filter('count',count)