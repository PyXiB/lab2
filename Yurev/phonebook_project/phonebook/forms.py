from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number']
        labels = {
            'name': 'Имя',
            'phone_number': 'Номер телефона',
        }
