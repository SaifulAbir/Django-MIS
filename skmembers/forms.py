from django import forms
from django.core.exceptions import ValidationError
from resources import strings as common_strings
from . import strings as sk_strings
from accounts.models import User
from skleaders.forms import SkUserForm
from skleaders.models import GENDER_CHOICES
from skmembers.models import SkMemberProfile
from django.utils.translation import ugettext_lazy as _


class SkMemberUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (5, 'skLeader'),
        (6, 'skMember'),
    )
    class_choice = (
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ("10", '10'),
    )
    first_name = forms.CharField(error_messages={'required': sk_strings.NAME_REQUIRED})
    user_type = forms.ChoiceField(required=False, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'user_type',)

class EditSkMemberUserForm(forms.ModelForm):
    first_name = forms.CharField(error_messages={'required': sk_strings.NAME_REQUIRED})
    user_type = forms.ChoiceField(required=False, choices=SkMemberUserForm.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))

    class Meta:
        model = User
        fields = ('first_name', 'email', 'user_type')



class SkMemberProfileForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    image = forms.ImageField(label=_(sk_strings.SKMEMBER_IMAGE_TEXT), required=False,
                             error_messages={'invalid': _(sk_strings.IMAGE_ERROR_MSG)}, widget=forms.FileInput)
    roll = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'type':'number'}))
    student_class = forms.ChoiceField(required=False,
                                      choices=SkMemberUserForm.class_choice, widget=forms.Select())
    mobile = forms.CharField(required=False, error_messages={'max_length': sk_strings.MOBILE_LENGTH_EXCEED},
                             widget=forms.TextInput(attrs={'type':'number'}))
    joining_date = forms.DateField(error_messages={'required': sk_strings.FROM_DATE_REQUIRED})
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class','joining_date', 'roll', 'school', 'gender', 'image_base64')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(sk_strings.IMAGE_FILE_SIZE_EXCEED)
            return image

class SkMemberProfileFormSkleader(forms.ModelForm):

    image = forms.ImageField(label=_(sk_strings.SKMEMBER_IMAGE_TEXT), required=False,
                             error_messages={'invalid': _(sk_strings.IMAGE_ERROR_MSG)}, widget=forms.FileInput)
    roll = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'type':'number'}))
    student_class = forms.ChoiceField(required=False,
                                      choices=SkMemberUserForm.class_choice, widget=forms.Select())
    mobile = forms.CharField(required=False, error_messages={'max_length': sk_strings.MOBILE_LENGTH_EXCEED}, widget=forms.TextInput(attrs={'type':'number'}))
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    joining_date = forms.DateField(error_messages={'required': sk_strings.FROM_DATE_REQUIRED})
    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class','joining_date','roll', 'gender')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(sk_strings.IMAGE_FILE_SIZE_EXCEED)
            return image

class SkMemberProfileFormForSkleader(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    image = forms.ImageField(label=_(sk_strings.SKMEMBER_IMAGE_TEXT), required=False,
                             error_messages={'invalid': _(sk_strings.IMAGE_ERROR_MSG)}, widget=forms.FileInput)
    roll = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'type':'number'}))
    student_class = forms.ChoiceField(required=False,
                                      choices=SkMemberUserForm.class_choice, widget=forms.Select())
    mobile = forms.CharField(required=False,error_messages={'max_length': sk_strings.MOBILE_LENGTH_EXCEED}, widget=forms.TextInput(attrs={'type':'number'}))
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    joining_date = forms.DateField(error_messages={'required': sk_strings.FROM_DATE_REQUIRED})
    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class', 'roll','joining_date', 'gender', 'image_base64')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(sk_strings.IMAGE_FILE_SIZE_EXCEED)
            return image

class EditSkMemberProfileForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    mobile = forms.CharField(required=False,error_messages={'max_length': sk_strings.MOBILE_LENGTH_EXCEED}, widget=forms.TextInput(attrs={'type':'number'}))

    joining_date = forms.DateField(error_messages={'required': sk_strings.FROM_DATE_REQUIRED})

    roll = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'type':'number'}))

    student_class = forms.ChoiceField(required=False,
                                      choices=SkUserForm.class_choice, widget=forms.Select())
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    image = forms.ImageField(label=_(sk_strings.SKMEMBER_IMAGE_TEXT), required=False,
                             error_messages={'invalid': _(sk_strings.IMAGE_ERROR_MSG)}, widget=forms.FileInput)

    joining_date = forms.DateField(required=False)
    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class', 'roll','gender', 'image_base64', 'joining_date')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(sk_strings.IMAGE_FILE_SIZE_EXCEED)
            return image