from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, NextOfKin, UserInformation
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "username")

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = []

class NextOfKinForm(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = []