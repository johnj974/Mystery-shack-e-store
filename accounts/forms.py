#  generate login form
from django import forms
#  generate user model
from django.contrib.auth.models import User
#  generate a new user form and validation
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# basic login form
class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)


# registration form to create new user
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)


# inner class to provide information about the form
class Meta:
    model = User
    fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name']


# e-mail validation
def clean_email(self):
    email = self.cleaned_data.get('email')
    username = self.cleaned_data.get('username')
    if User.objects.filter(email=email).exclude(username=username):
        raise forms.ValidationError(u'Email address must be unique')
    return email

# password validation
def clean_password2(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')

        
    if not password1 or not password2:
        raise ValidationError("Please confirm your password")
        
    if password1 != password2:
        raise ValidationError("Passwords must match")
        
    return password2
