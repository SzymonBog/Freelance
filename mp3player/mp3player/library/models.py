from django.db import models

# Create your models here.
class Music(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

