from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE

from users.models import UserProfile


class Art(models.Model):
    ABSTRACT = 'abstract'
    CARTOON = 'cartoon'
    GRAFFITI = 'graffiti'
    OTHER = 'other'

    ART_TYPES = (
        (ABSTRACT, 'Abstract'),
        (CARTOON, 'Cartoon'),
        (GRAFFITI, 'Graffiti'),
        (OTHER, 'Other'),
    )

    name = models.CharField(max_length=60)
    artist = models.CharField(max_length=120)
    type = models.CharField(choices=ART_TYPES, default=OTHER, max_length=8)
    image = models.ImageField(upload_to='media')

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class EditArt(models.Model):
    ABSTRACT = 'abstract'
    CARTOON = 'cartoon'
    GRAFFITI = 'graffiti'
    OTHER = 'other'

    ART_TYPES = (
        (ABSTRACT, 'Abstract'),
        (CARTOON, 'Cartoon'),
        (GRAFFITI, 'Graffiti'),
        (OTHER, 'Other'),
    )

    name = models.CharField(max_length=60, blank=True)
    artist = models.CharField(max_length=120, blank=True)
    type = models.CharField(choices=ART_TYPES, default=OTHER, max_length=8)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
