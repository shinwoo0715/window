from django.contrib.auth import get_user_model, forms as django_forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.hashers import check_password


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = (
        #     'email',
        #     'username',
        #     'password'
        # )
        fields = ('email' , 'username' , 'password')
