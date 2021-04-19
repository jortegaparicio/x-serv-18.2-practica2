from django.db import models

# Create your models here.


class Content(models.Model):
    shortUrl = models.TextField()
    url = models.TextField()
