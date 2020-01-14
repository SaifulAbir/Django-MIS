from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from headmasters.models import HeadmasterProfile
import accounts.strings as account_strings
from skleaders.models import SkLeaderProfile
import resources.strings as common_strings


class PrettyAuthenticationForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': account_strings.CLASS_FORM_CONTROL, 'placeholder': account_strings.USER_NAME_PLACEHOLDER}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': account_strings.CLASS_FORM_CONTROL, 'placeholder': account_strings.PASSWORD_PLACEHOLDER}))

    # def clean(self):
    #     user = self.authenticate_via_email()
    #     if not user:
    #         raise forms.ValidationError(account_strings.EMAIL_AUTHENTICATION_ERROR)
    #     else:
    #         self.user = user
    #     return self.cleaned_data
    #
    # def authenticate_via_email(self):
    #     """
    #         Authenticate user using email.
    #         Returns user object if authenticated else None
    #     """
    #     email = self.cleaned_data['email']
    #     if email:
    #         try:
    #             user = User.objects.get(email__iexact=email)
    #             if user.check_password(self.cleaned_data['password']):
    #                 return user
    #         except ObjectDoesNotExist:
    #             pass
    #         return None

class EditUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (1, account_strings.USER_TYPE_ADMIN)
    )
    first_name = forms.CharField(label=common_strings.USER_PROFILE_NAME)
    email = forms.CharField(label=common_strings.USER_PROFILE_USERNAME, error_messages={'required': account_strings.EMAIL_REQUIRED_ERROR})
    password = forms.CharField(label=common_strings.USER_PROFILE_PASSWORD,required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label=common_strings.USER_PROFILE_CONFIRM_PASSWORD,required=False, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(required=False, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    image = forms.ImageField(label=_(account_strings.USER_IMAGE_LEVEL_TEXT), required=False,
                             error_messages={'invalid': _(account_strings.USER_IMAGE_VALIDATION_ERROR)}, widget=forms.FileInput)
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type', 'image','image_base64')

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', account_strings.USER_CONFIRM_PASSWORD_ERROR)

        return cleaned_data

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(account_strings.USER_IMAGE_SIZE_ERROR)
            return image

class HeadmasterProfileForm(forms.ModelForm):
    image = forms.ImageField(label=_(account_strings.HEADMASTER_IMAGE_LEVEL_TEXT), required=False,
                             error_messages={'invalid': _(account_strings.USER_IMAGE_VALIDATION_ERROR)}, widget=forms.FileInput)
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = HeadmasterProfile
        fields = ('image','image_base64')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(account_strings.USER_IMAGE_SIZE_ERROR)
            return image

class SkleaderProfileForm(forms.ModelForm):
    image = forms.ImageField(label=_(account_strings.SKLEADER_IMAGE_LEVEL_TEXT), required=False,
                             error_messages={'invalid': _(account_strings.USER_IMAGE_VALIDATION_ERROR)}, widget=forms.FileInput)
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = SkLeaderProfile
        fields = ('image','image_base64')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(account_strings.USER_IMAGE_SIZE_ERROR)
            return image

