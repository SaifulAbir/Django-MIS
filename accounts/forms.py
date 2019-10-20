from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile


class PrettyAuthenticationForm(forms.Form):

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        user = self.authenticate_via_email()
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        else:
            self.user = user
        return self.cleaned_data

    def authenticate_via_email(self):
        """
            Authenticate user using email.
            Returns user object if authenticated else None
        """
        email = self.cleaned_data['email']
        if email:
            try:
                user = User.objects.get(email__iexact=email)
                if user.check_password(self.cleaned_data['password']):
                    return user
            except ObjectDoesNotExist:
                pass
            return None

class EditUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (1, 'admin')
    )
    email = forms.EmailField(error_messages={'required': 'Email is required.'})
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(required=False, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    image = forms.ImageField(label=_('User image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type', 'image',)

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match.")

        return cleaned_data

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image

class HeadmasterProfileForm(forms.ModelForm):
    image = forms.ImageField(label=_('Headmaster image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = HeadmasterProfile
        fields = ('image',)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image

class SkleaderProfileForm(forms.ModelForm):
    image = forms.ImageField(label=_('Headmaster image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = SkLeaderProfile
        fields = ('image',)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password confirmation'}),
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2
