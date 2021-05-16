from django import forms
from .models import Musicapp2

class Musicapp2Form(forms.ModelForm):
    class Meta:
        model = Musicapp2
        fields = ['title', 'writer', 'body', 'image']

