from django import forms
from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from basicapp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
   

    class Meta():
        model = User
        exclude = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

