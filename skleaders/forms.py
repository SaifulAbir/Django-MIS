from django import forms
from django.core.exceptions import ValidationError
from django.template import Template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from school.models import School
from skleaders.models import SkLeaderProfile, GENDER_CHOICES
from django.utils.translation import ugettext_lazy as _
from . import strings as skleader_strings
from resources import strings as common_strings




class SkUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (5, skleader_strings.SK_LEADER),
        (6, skleader_strings.SK_MEMBER),
    )

    class_choice = (

        ('', '--Select--'),

        ('6', '6'),

        ('7', '7'),

        ('8', '8'),

        ('9', '9'),

        ("10", '10'),)
<<<<<<< HEAD
<<<<<<< HEAD
    first_name = forms.CharField(error_messages={'required': skleader_strings.NAME_REQUIRED})

    password = forms.CharField(error_messages={'required': skleader_strings.PASSWORD_REQUIRED},
=======
    first_name = forms.CharField(error_messages={'required': 'Name is required.'})

    password = forms.CharField(error_messages={'required': 'Password is required.'},
>>>>>>> features/admin_skmember
=======
    first_name = forms.CharField(error_messages={'required': skleader_strings.NAME_REQUIRED})

    password = forms.CharField(error_messages={'required': skleader_strings.PASSWORD_REQUIRED},
>>>>>>> feature/hotfix_0.9
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    confirm_password = forms.CharField(error_messages={'required': skleader_strings.CONFIRM_PASSWORD_REQUIRED},
                                       widget=forms.PasswordInput())
    user_type = forms.ChoiceField(required=False, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type',)

    def clean(self):
        cleaned_data = super(SkUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', skleader_strings.PASSWORD_NOT_MATCHED)

        return cleaned_data

class EditSkUserForm(forms.ModelForm):
<<<<<<< HEAD
<<<<<<< HEAD
    first_name = forms.CharField(error_messages={'required': skleader_strings.NAME_REQUIRED})
=======
    first_name = forms.CharField(error_messages={'required': 'Name is required.'})
>>>>>>> features/admin_skmember
=======
    first_name = forms.CharField(error_messages={'required': skleader_strings.NAME_REQUIRED})
>>>>>>> feature/hotfix_0.9
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(required=False, choices=SkUserForm.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(EditSkUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', skleader_strings.PASSWORD_NOT_MATCHED)

        return cleaned_data


class SkLeaderProfileForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    mobile = forms.CharField(error_messages={'required': skleader_strings.MOBILE_REQUIRED},
                             widget=forms.TextInput(attrs={'type':'number'}))

    joining_date = forms.DateField(error_messages={'required': skleader_strings.FROM_DATE_REQUIRED})

    roll = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'number'}))

    student_class = forms.ChoiceField(required=False,
                                      choices=SkUserForm.class_choice, widget=forms.Select())
    image = forms.ImageField(required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    school = forms.ModelChoiceField(error_messages={'required': skleader_strings.SCHOOL_REQUIRED}, queryset=School.objects.all())
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)

    class Meta:
        model = SkLeaderProfile
        fields = ('mobile', 'image', 'student_class', 'roll', 'school','joining_date','emergency_contact_person','emergency_contact_number', 'gender', 'image_base64')

    def clean(self):
        cleaned_data = super().clean()
        mobile = cleaned_data.get("mobile")

        if mobile:
            if len(mobile)>11:
                msg = skleader_strings.MOBILE_LENGTH_EXCEED
                self.add_error('mobile', msg)
    def clean_image(self):

        image = self.cleaned_data.get('image', False)

        if image:

            if image.size > 1 * 1024 * 1024:
                raise ValidationError(skleader_strings.IMAGE_SIZE_EXCEED)

            return image

class EditSkLeaderProfileForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    mobile = forms.CharField(error_messages={'required': skleader_strings.MOBILE_REQUIRED,
                                             'max_length': skleader_strings.MOBILE_LENGTH_EXCEED},
                             widget=forms.TextInput(attrs={'type':'number'}))

    joining_date = forms.DateField(error_messages={'required': skleader_strings.FROM_DATE_REQUIRED})

    roll = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'type':'number'}))

    student_class = forms.ChoiceField(required=False,
                                      choices=SkUserForm.class_choice, widget=forms.Select())
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    image = forms.ImageField(label=_('Skleader image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    joining_date = forms.DateField(required=False)
    class Meta:
        model = SkLeaderProfile
        fields = ('mobile', 'image', 'student_class', 'roll','joining_date', 'emergency_contact_person','emergency_contact_number', 'gender', 'image_base64')

    def clean(self):
        cleaned_data = super().clean()
        mobile = cleaned_data.get("mobile")

        if mobile:
            if len(mobile)>11:
                msg = skleader_strings.MOBILE_LENGTH_EXCEED
                self.add_error('mobile', msg)
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(skleader_strings.IMAGE_SIZE_EXCEED)
            return image