import re
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from datetime import date
from resources import strings


def check_valid_chars(value):
    regex = re.compile('[@\\\_!\-#$%^&*()<>?/\|}{~:,\[\]+.=\'"0-9]')
    if not regex.search(value) == None:
        raise ValidationError(strings.VALIDATION_CHAR_ERROR_MESSEGE)

def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError(strings.FUTURE_DATE_VALIDATION_ERROR_MESSEGE)
