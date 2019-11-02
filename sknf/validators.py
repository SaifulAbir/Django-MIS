import re
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from datetime import date

def check_valid_chars(value):
    regex = re.compile('[@\\\_!\-#$%^&*()<>?/\|}{~:,\[\]+.=\'"0-9]')
    if not regex.search(value) == None:
        raise ValidationError('Invalid Validation')

def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('This Date cannot be in the future.')
