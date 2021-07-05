from django import forms
from .models import Cookierun

class CookierunForm(forms.ModelForm):
    class Meta:
        model = Cookierun
        fields = ['title', 'writer', 'body', 'image']

