from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE



class Art(models.Model):
    name = models.CharField(max_length=60)
    artist = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media')
    # user = models.ForeignKey(UserProfile, on_delete=CASCADE)