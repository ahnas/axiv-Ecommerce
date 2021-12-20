from django import forms
from django.db.models import fields
from core.models import Order
from .models import Contact,ServiceEnquiry,Email,Feedback
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
        
class ServiceEnquiryForm(forms.ModelForm):
    class Meta:
        model = ServiceEnquiry
        fields = '__all__'
        widgets = {
            'intrestedProduct': TextInput(attrs={'class': 'form-control', 'placeholder': 'Intrested Product'}),
            'firstname': TextInput(attrs={'class': 'form-control', 'placeholder': 'FirstName'}),
            'lastname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Lastname'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'jobTitile': TextInput(attrs={'class': 'form-control', 'placeholder': 'job Titile'}),
            'companyName': TextInput(attrs={'class': 'form-control', 'placeholder': 'company Name'}),
            'country': Select(attrs={'class': 'form-control', 'placeholder': 'country'}),
            'industry': TextInput(attrs={'class': 'form-control', 'placeholder': 'industry'}),
            'jobFunction': TextInput(attrs={'class': 'form-control', 'placeholder': 'job Function'}),
            'corporateLevel': TextInput(attrs={'class': 'form-control', 'placeholder': 'corporate Level'}),
            'natureOfInquiry': TextInput(attrs={'class': 'form-control', 'placeholder': 'nature Of Inquiry'}),
        }
    
class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        widgets = {
            
            'email': EmailInput(attrs={'class': 'required form-control', 'placeholder': 'Your Email Address'}),
            
        }



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            
            'message': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Feed Back','rows':'7'}),

        }



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your number'}),
            'address': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Type Your address'}),
        } 