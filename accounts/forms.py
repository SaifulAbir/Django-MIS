from django import forms
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import User


class PrettyAuthenticationForm(forms.Form):

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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

