from django.template.defaulttags import register

@register.filter
def get_post_Cat(dictionary, key):
    return dictionary.get(str(key))
