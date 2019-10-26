from django import forms

from topics.models import Topics
from .models import ClassOrientation

class ClassOrientationForm(forms.ModelForm):
    topic = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=False)
    created_date = forms.DateField(error_messages={'required': 'Date is required.'}, widget=forms.DateInput(format='%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    class Meta:
        model = ClassOrientation
        fields = ['created_date', 'student_class', 'topic']
