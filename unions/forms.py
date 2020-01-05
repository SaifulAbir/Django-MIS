from django import forms

from upazillas.models import Upazilla
from .models import Union
import unions.strings as union_strings


class UnionForm(forms.ModelForm):
    name = forms.CharField(label=union_strings.UNION_NAME)
    upazilla = forms.ModelChoiceField(label=union_strings.FORM_LABEL_UPAZILA, queryset=Upazilla.objects.all())
    class Meta:
        model = Union
        fields = ['division','district','upazilla','name']

