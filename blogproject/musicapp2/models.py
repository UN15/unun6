from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Musicapp2(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="mblog2/", blank=True, null=True)
    thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(150, 150)], format = "JPEG")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
