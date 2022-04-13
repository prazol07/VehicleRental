from django import forms
from dataclasses import field
from .models import *

class VehicleRentForm(forms.ModelForm):
    class Meta:
        model = VehicleRent
        exclude=('is_booked',)
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'vehiclenumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_image': forms.FileInput(attrs={'class': 'form-control'}),
            'bluebook_image': forms.FileInput(attrs={'class': 'form-control'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class VehicleBookForm(forms.ModelForm):
    class Meta:
        model = VehicleBook
        exclude=('user',)
        widgets = {
            'rent_info': forms.Select(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'vehicle_name': forms.NumberInput(attrs={'class': 'form-control'}),
            'renting_days': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }
