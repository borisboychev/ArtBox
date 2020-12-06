from django import forms

from art.models import ContactUs, Art


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        fields = '__all__'


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.ImageField(),
        }
        fields = '__all__'