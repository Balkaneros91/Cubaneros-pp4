from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from .models import Booking
from .widget import DatePickerInput, TimePickerInput
from datetime import time


def validate_opening_hours(value):
    opening_time = time(14, 0)
    closing_time = time(23, 0)
    last_booking_time = closing_time.replace(hour=closing_time.hour-2, minute=0, second=0, microsecond=0)

    if not (opening_time <= value <= closing_time):
        raise forms.ValidationError("Please select a time within opening hours (2pm - 11pm).")
    elif value > last_booking_time:
        raise forms.ValidationError("Sorry, the last online booking can be made at most 2 hours before closing time.")


class BookingForm(forms.ModelForm):
    reservation_time = forms.TimeField(widget=TimePickerInput(attrs={'class': 'form-control'}), validators=[validate_opening_hours])

    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'number_of_guests', 'reservation_date', 'reservation_time', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'number_of_guests': forms.NumberInput(attrs={'min': 1, 'max': 8}),
            'reservation_date': DatePickerInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter any special request'}),
        }