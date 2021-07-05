from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class Acc_registerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password1', 'password2', 'nickname', 'guildname', 'location' ]