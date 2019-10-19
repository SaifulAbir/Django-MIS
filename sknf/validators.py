import re
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

def check_valid_chars(value):
    regex = re.compile('[@\\\_!\-#$%^&*()<>?/\|}{~:,\[\]+.=\'"0-9]')
    if not regex.search(value) == None:
        raise ValidationError('Invalid Validation')
