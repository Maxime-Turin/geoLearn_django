from django import forms
from .models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'capital_city', 'population',
                  'official_language', 'continent', 'flag')
