from django import template

register = template.Library()

@register.filter()
def media_file(shot_path):
    if shot_path:
        return f'/media/{shot_path}'
    else:
        return '#'


#
# @register.tags()
# def media_file(shot_path):
#     if shot_path:
#         return f'/media/{shot_path}'
#     else:
#         return '#'