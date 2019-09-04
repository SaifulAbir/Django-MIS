from django import forms

from school.models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'school_id', 'division', 'district', 'upazilla', 'union', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.7em;'}),
        }