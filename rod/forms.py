from django import forms
from .models import Drony

class DronUpdateForm(forms.ModelForm):
    class Meta:
        model = Drony
        fields = '__all__'

