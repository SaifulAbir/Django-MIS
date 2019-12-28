from django.template.defaultfilters import register


@register.filter(name='format')
def format(format, value):
    return format % value


@register.simple_tag
def format_values(format, *args):
    return format % args