from django import forms
from django.contrib.auth.models import User


# basic login form
class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)