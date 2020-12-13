from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # UserCreationForm already includes password

        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)  # If no email default value will be False
        print(email)
        if email:
            if re.match(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+', self.cleaned_data['email']):
                return email
            else:
                raise forms.ValidationError("Email not valid")
        else:
            raise forms.ValidationError("Email field required")

