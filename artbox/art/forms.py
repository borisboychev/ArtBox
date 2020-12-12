from django import forms
from django.contrib.auth.models import User

from art.models import Art, EditArt
from users.models import UserProfile


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}),
        }
        user = UserProfile.user
        fields = ('name', 'artist', 'image', 'type')


class EditArtForm(forms.ModelForm):
    class Meta:
        model = EditArt
        fields = ('name', 'artist', 'type')