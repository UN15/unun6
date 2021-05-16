from django import forms
from .models import Musicapp

class MusicappForm(forms.ModelForm):
    class Meta:
        model = Musicapp
        fields = ['title', 'writer', 'body']

