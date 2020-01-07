from django import forms

from upazillas.models import Upazilla
from . import strings as upazilla_strings

class UpazillaForm(forms.ModelForm):
    class Meta:
        model = Upazilla
        fields = ['division', 'district', 'name']

