from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

'''
A custom form for the user signup process.
'''


class SignupForm(UserCreationForm):
    is_trainer = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_trainer')