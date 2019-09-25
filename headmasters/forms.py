from django import forms
from django.forms import DateField
from sknf import settings

from accounts.models import User
from .models import HeadmasterProfile, HeadmasterDetails
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (2, 'headmaster'),
        (3, 'Guide Teacher'),
        (4, 'both'),
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}), initial='2')
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match.")

        return cleaned_data

class EditUserForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(choices=UserForm.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match.")

        return cleaned_data


class HeadmasterProfileForm(forms.ModelForm):
    image = forms.ImageField(label=_('Headmaster image'), required=False,
                                    error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    joining_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = HeadmasterProfile
        fields = ('mobile','school', 'image','joining_date')

class HeadmasterDetailsForm(forms.ModelForm):

    class Meta:

        model = HeadmasterDetails
        fields = ('from_date', 'school', 'to_date')
