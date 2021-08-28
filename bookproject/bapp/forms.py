from django import forms
from .models import Bapp

class BappForm(forms.ModelForm):
    class Meta:
        model = Bapp
        fields = ['title', 'writer', 'body', 'image']

class PostSearchForm(forms.Form):
    search_word=forms.CharField(label='Search Word')