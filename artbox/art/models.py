from django.db import models

# Create your models here.
class ContactUs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()


class Art(models.Model):
    name = models.CharField(max_length=60)
    artist = models.CharField(max_length=120)
    image = models.ImageField()