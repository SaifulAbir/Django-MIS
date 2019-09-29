from django import forms

from districts.models import District
from school.models import School
from unions.models import Union
from upazillas.models import Upazilla
from django.utils.translation import ugettext_lazy as _


class SchoolForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required': 'Your name is required.'})
    class Meta:
        model = School
        fields = ['name', 'school_id', 'division', 'district', 'upazilla', 'union', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.51em;'}),

        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['district'].queryset = District.objects.none()
    #     self.fields['upazilla'].queryset = Upazilla.objects.none()
    #     self.fields['union'].queryset = Union.objects.none()

class EditSchoolForm(forms.ModelForm):
    image = forms.ImageField(label=_('SkMember image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = School
        fields = ['image']

