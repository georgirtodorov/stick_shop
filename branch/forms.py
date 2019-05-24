from django import forms
from django.core.validators import MinValueValidator

from .models import MagicWand, Survachki, Fetchers


class CreateMagicWandForm(forms.ModelForm):

    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    price = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))
    magic_power = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))
    category = 'wizzard'

    class Meta:
        model = MagicWand
        fields = ('id', 'image_url', 'name', 'price', 'magic_power',)


class CreateFetchersForm(forms.ModelForm):

    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    price = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))
    barkness = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))

    happiness = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))

    category = 'GoodBois'
    class Meta:
        model = Fetchers
        fields = ('id', 'image_url', 'name', 'price', 'barkness', 'happiness',)


class CreateSurvachkiForm(forms.ModelForm):

    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    price = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))
    money_income = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'number'
                                   }
                               ))

    category = 'survacane'
    class Meta:
        model = Survachki
        fields = ('id', 'image_url', 'name', 'price', 'money_income')