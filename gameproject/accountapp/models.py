from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    nickname= models.CharField(max_length=100)
    guildname = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
