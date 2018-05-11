from django import forms
from django.core.validators import EmailValidator

from twitter_app.models import Twitt


class AddTwittForm(forms.ModelForm):
    class Meta:
        model = Twitt
        fields = ['content']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='user-name')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='password2')
    first_name = forms.CharField(label='first-name')
    last_name = forms.CharField(label='last-name')
    email = forms.CharField(label='user-email', validators=[EmailValidator(message='wrong email')])
