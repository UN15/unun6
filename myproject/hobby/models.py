from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Hobby(models.Model):
    title=models.CharField(max_length=200)
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to="hobby/", blank=True, null=True)
    thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(200,200)], format = "JPEG")   
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class Message(models.Model):
    title=models.CharField(max_length=200)
    to=models.CharField(max_length=100)
    sender=models.CharField(max_length=100)
    body=models.TextField()
    
    def summary(self):
        return self.body[:30]



