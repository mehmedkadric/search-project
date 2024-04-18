from django import forms
from .models import Search, Data

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['query']
        widgets = {
            'query': forms.TextInput(attrs={'placeholder': 'Enter text here', 'class' : 'form-control'})
        }


class UploadDataForm(forms.ModelForm):
    data_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': '.xls,.xlsx,.csv'}))

    class Meta:
        model = Data
        fields = ['data_file']