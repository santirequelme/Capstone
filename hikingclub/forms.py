from django import forms
from .models import Booking
from django.forms import ModelForm, DateInput, TextInput, NumberInput

class booking_form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'last_name','date', 'phone')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'type your name here', 'id':'namel'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'type your lastname here'
            }),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'size':'16', 'id':'datetime'
            }),
            'phone': NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Phonenumber', 'type':'Number'
            })
        }