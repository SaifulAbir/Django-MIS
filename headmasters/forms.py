from PIL import Image
from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateField

from school.models import School
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
    email = forms.EmailField(error_messages={'required': 'Email is required.'})
    password = forms.CharField(error_messages={'required': 'Password is required.'}, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(error_messages={'required': 'Confirm password is required.'}, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(error_messages={'required': 'User type is required.'}, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
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
    email = forms.EmailField(error_messages={'required': 'Email is required.'})
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(error_messages={'required': 'User type is required.'}, choices=UserForm.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
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
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())

    image = forms.ImageField(label=_('Headmaster image'), required=False,
                                    error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    joining_date = DateField(error_messages={'required': 'From date is required.'})
    mobile = forms.CharField(error_messages={'required': 'Mobile is required.'})
    school = forms.ModelChoiceField(error_messages={'required': 'School is required.'}, queryset=School.objects.all())

    class Meta:
        model = HeadmasterProfile
        fields = ('mobile','school', 'image','joining_date', 'image_base64')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image

    # def save(self, commit=True):
    #     new_image = super(HeadmasterProfileForm, self).save(commit=False)
    #
    #     x = self.cleaned_data.get('x')
    #     y = self.cleaned_data.get('y')
    #     w = self.cleaned_data.get('width')
    #     h = self.cleaned_data.get('height')
    #
    #     image = Image.open(new_image.image)
    #     cropped_image = iimage.crop((x, y, w + x, h + y))
    #     resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
    #     resized_image.save(new_image.image.path)
    #
    #     return new_image

class HeadmasterDetailsForm(forms.ModelForm):

    class Meta:
        model = HeadmasterDetails
        fields = ('from_date', 'school', 'to_date')



