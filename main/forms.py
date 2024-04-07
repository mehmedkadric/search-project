# forms.py

from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['query']
        widgets = {
            'query': forms.TextInput(attrs={'placeholder': 'Enter text here'})
        }
