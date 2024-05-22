from django import template

register = template.Library()


@register.simple_tag
def my_media(data):
    if data:
        return f'/media/image/{data}'
    return '#'


"""# Создание фильтра
@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)"""
