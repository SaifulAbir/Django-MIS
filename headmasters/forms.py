from PIL import Image
from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateField

from school.models import School
from sknf import settings
from . import strings as headmaster_strings
from accounts.models import User
from .models import HeadmasterProfile, HeadmasterDetails
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (2, headmaster_strings.HEADMASTER),
        (3, headmaster_strings.GUIDE_TEACHER),
        (4, headmaster_strings.BOTH),
    )
    first_name = forms.CharField(error_messages={'required': headmaster_strings.NAME_REQUIRED})
    password = forms.CharField(error_messages={'required': headmaster_strings.PASSWORD_REQUIRED}, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(error_messages={'required': headmaster_strings.CONFIRM_PASSWORD_REQUIRED}, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(error_messages={'required': headmaster_strings.USER_TYPE_REQUIRED}, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', headmaster_strings.PASSWORD_NOT_MATCHED)

        return cleaned_data

class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(error_messages={'required': headmaster_strings.NAME_REQUIRED})
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(error_messages={'required': headmaster_strings.USER_TYPE_REQUIRED}, choices=UserForm.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', headmaster_strings.PASSWORD_NOT_MATCHED)

        return cleaned_data


class HeadmasterProfileForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())

    image = forms.ImageField(required=False,
                                    error_messages={'invalid': _(headmaster_strings.IMAGE_FILE_ONLY)}, widget=forms.FileInput)
    joining_date = DateField(error_messages={'required': headmaster_strings.FROM_DATE_REQUIRED})
    mobile = forms.CharField(error_messages={'required': headmaster_strings.MOBILE_REQUIRED,'max_length': headmaster_strings.MOBILE_LENGTH_EXCEED},
                             widget=forms.TextInput(attrs={'type':'number'}))
    school = forms.ModelChoiceField(error_messages={'required': headmaster_strings.SCHOOL_REQUIRED}, queryset=School.objects.all())

    class Meta:
        model = HeadmasterProfile
        fields = ('mobile','school', 'image','joining_date', 'image_base64')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(headmaster_strings.IMAGE_FILE_SIZE_EXCEED)
            return image

class EditHeadmasterProfileForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())

    image = forms.ImageField(required=False,
                                    error_messages={'invalid': _(headmaster_strings.IMAGE_FILE_ONLY)}, widget=forms.FileInput)
    joining_date = DateField(required=False, error_messages={'required': headmaster_strings.FROM_DATE_REQUIRED})
    mobile = forms.CharField(error_messages={'required': headmaster_strings.MOBILE_REQUIRED,'max_length': headmaster_strings.MOBILE_LENGTH_EXCEED},
                             widget=forms.TextInput(attrs={'type':'number'}))

    class Meta:
        model = HeadmasterProfile
        fields = ('mobile', 'image','joining_date', 'image_base64')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(headmaster_strings.IMAGE_FILE_SIZE_EXCEED)
            return image



class HeadmasterDetailsForm(forms.ModelForm):

    class Meta:
        model = HeadmasterDetails
        fields = ('from_date', 'school', 'to_date')



