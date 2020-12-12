from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='user_pictures', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class EditProfile(models.Model):
    profile_picture = models.ImageField(upload_to='user_pictures', blank=True)
    username = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)