from django import forms

from art.models import ContactUs


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