from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import UserProfile, EditProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = EditProfile
        fields = "__all__"