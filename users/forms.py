from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username']
        labels = {
            'first_name': 'Imie',
            'last_name': 'Nazwisko',
            'username': 'Nazwa użytkownika',
            'email': 'Email',
        }
        help_texts = {
            'username': None,
        }