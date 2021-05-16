from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Musicapp(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=50)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]