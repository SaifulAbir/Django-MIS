from django import forms

from districts.models import District
from school.models import School
from unions.models import Union
from upazillas.models import Upazilla


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'school_id', 'division', 'district', 'upazilla', 'union', 'address']
        # widgets = {
        #     'address': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.7em;'}),
        #     'name': forms.TextInput(
        #         attrs={'pattern': "[a-zA-Z\s]+", 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')",
        #                'style': ''}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['district'].queryset = District.objects.none()
    #     self.fields['upazilla'].queryset = Upazilla.objects.none()
    #     self.fields['union'].queryset = Union.objects.none()

