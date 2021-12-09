from django import forms
from django.db.models import fields
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'email': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Email Address'}),
            'subject': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Type Your Message'}),
        }
        