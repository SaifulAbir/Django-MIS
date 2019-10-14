from django import forms
from .models import ClassOrientation

class ClassOrientationForm(forms.ModelForm):
    created_date = forms.DateField(error_messages={'required': 'Date is required.'}, widget=forms.DateInput(format='%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    class Meta:
        model = ClassOrientation
        fields = ['created_date', 'student_class', 'topic']
