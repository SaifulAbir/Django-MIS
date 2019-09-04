from django import forms

from school.models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['division', 'name']