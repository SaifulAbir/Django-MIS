from django import forms
from .models import Union
import unions.strings as union_strings


class UnionForm(forms.ModelForm):
    name = forms.CharField(label=union_strings.UNION_NAME)
    class Meta:
        model = Union
        fields = ['division','district','upazilla','name']

