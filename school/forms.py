from django import forms
import school.strings as school_strings
from districts.models import District
from school.models import School, SchoolPost
from unions.models import Union
from upazillas.models import Upazilla
from django.utils.translation import ugettext_lazy as _


class SchoolForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required': 'School name is required.'})
    school_id = forms.CharField(label='EIIN',error_messages={'required': 'EIIN is required.', 'unique': 'School with this EIIN already exists.'},
                                widget=forms.TextInput(attrs={'type':'text'}))
    club_establishment_date = forms.DateField(label='dd-mm-yyyy',error_messages={'required': 'Date is required.'},
                                   widget=forms.DateInput(format='%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    class Meta:
        model = School
        fields = ['name', 'school_id','club_establishment_date', 'division', 'district', 'upazilla', 'union', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.51em;'}),

        }

class EditSchoolForm(forms.ModelForm):
    cover_image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    image = forms.ImageField(label=_('SkMember image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
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

