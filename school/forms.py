from django import forms
import school.strings as school_strings
from districts.models import District
from school.models import School, SchoolPost
from unions.models import Union
from upazillas.models import Upazilla
from django.utils.translation import ugettext_lazy as _


class SchoolForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required': school_strings.SCHOOL_NAME_REQUIRED_ERROR_MSG})
    school_id = forms.CharField(label=school_strings.SCHOOL_LIST_EIIN_TEXT,error_messages={'required': school_strings.SCHOOL_EIIN_REQUIRED_ERROR_MSG, 'unique': school_strings.SCHOOL_EIIN_UNIQUE_ERROR_MSG},
                                widget=forms.TextInput(attrs={'type':'text'}))
    club_establishment_date = forms.DateField(label=school_strings.DATE_LABEL_TEXT,error_messages={'required': school_strings.SCHOOL_DATE_REQUIRED_ERROR_MSG},
                                   widget=forms.DateInput(format='%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    class Meta:
        model = School
        fields = ['name', 'school_id','club_establishment_date', 'division', 'district', 'upazilla', 'union', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.51em;'}),

        }

class EditSchoolForm(forms.ModelForm):
    cover_image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    image = forms.ImageField(required=False,
                             error_messages={'invalid': _(school_strings.HOME_IMAGE_VALIDATION_ERROR)}, widget=forms.FileInput)
    class Meta:
        model = School
        fields = ['image', 'cover_image_base64']

class SchoolPostForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    post_image = forms.ImageField(required=False,
                             error_messages={'invalid': _(school_strings.HOME_IMAGE_VALIDATION_ERROR)}, widget=forms.FileInput)
    class Meta:
        model = SchoolPost
        fields = ['text','post_image', 'image_base64']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': school_strings.HOME_POST_TEXT_STYLE, 'placeholder':school_strings.HOME_SCHOOL_POST_PLACEHOLDER}),}

class SchoolUpdatePostForm(forms.ModelForm):
    image_base = forms.CharField(required=False, widget=forms.HiddenInput())
    post_image = forms.ImageField(required=False,
                             error_messages={'invalid': _(school_strings.HOME_IMAGE_VALIDATION_ERROR)}, widget=forms.FileInput)
    class Meta:
        model = SchoolPost
        fields = ['text','post_image', 'image_base']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': school_strings.HOME_POST_TEXT_STYLE, 'placeholder':school_strings.HOME_SCHOOL_POST_PLACEHOLDER}),}

