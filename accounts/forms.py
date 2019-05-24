from django import forms
from .models import ProfileUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password', 'email')


class ProfileUserForm(forms.ModelForm):
     class Meta():
         model = ProfileUser
         fields = ('profile_pic',)