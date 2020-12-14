from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {
            'first_name': 'Imie',
            'last_name': 'Nazwisko',
            'username': 'Nazwa użytkownika',
            'email': 'Email',
        }
        help_texts = {
            'username': None,
        }
