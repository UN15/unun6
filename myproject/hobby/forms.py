from django import forms
from .models import Hobby, Message

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['title', 'writer', 'body', 'image']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'to', 'sender', 'body']


