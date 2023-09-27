from django import template

register = template.Library()

@register.filter()
def media_file(shot_path):
    if shot_path:
        return f'/{shot_path}'
    else:
        return '#'



@register.simple_tag()
def media_file(shot_path):
    if shot_path:
        return f'/{shot_path}'
    else:
        return '#'