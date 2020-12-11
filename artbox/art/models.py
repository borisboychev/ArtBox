from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


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


class Comment(models.Model):
    pet = models.ForeignKey(Art, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
