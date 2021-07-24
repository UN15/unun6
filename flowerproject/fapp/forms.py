from django import forms
from .models import Fapp

class FappForm(forms.ModelForm):
    class Meta:
        model = Fapp
        fields = ['title', 'writer', 'body', 'image']

class PostSearchForm(forms.Form):
    search_word=forms.CharField(label='Search Word')

