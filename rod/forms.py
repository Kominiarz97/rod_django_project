from django import forms
from .models import Drony, Trasy

class DronUpdateForm(forms.ModelForm):
    class Meta:
        model = Drony
        fields = '__all__'


class RouteUpdateForm(forms.ModelForm):
    class Meta:
        model = Trasy
        fields = '__all__'
        labels = {
            'nazwa_trasy': 'Nazwa trasy',
            'stacja_poczatek': 'Stacja początkowa',
            'stacja_koniec': 'Stacja końcowa',
            'dlugosc_trasy': 'Długość trasy'
        }



