from django.db import models

# Create your models here.


class Content(models.Model):
    shorturl = models.TextField()
    url = models.TextField()
