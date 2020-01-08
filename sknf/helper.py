from django.db.models import ProtectedError
from django.template.defaultfilters import register


@register.filter(name='format')
def format(format, value):
    return format % value


@register.simple_tag
def format_values(format, *args):
    return format % args

@register.simple_tag
def format_date(format, value):
    return value.strftime(format)

def check_child_data_exist_on_delete(model):
    try:
        model.delete()
        status = True
    except ProtectedError:
        status = False
    return status