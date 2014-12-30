__author__ = 'rbonick'

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Registration form for new users
class UserRegistrationForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']