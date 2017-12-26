from django import forms
from .models import input

class HomeForm(forms.ModelForm):
    class Meta:
        model = input
        fields = {'visitorControl','visitorVariation','conversionControl','conversionVariation'}



