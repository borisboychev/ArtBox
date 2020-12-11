from django import forms

from art.models import Art

class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}),
        }
        fields = '__all__'