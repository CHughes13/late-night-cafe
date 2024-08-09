from django import forms
from django.contrib.auth.forms import UserCreationForm # Import Django's built-in UserCreationForm
from django.contrib.auth.models import User # Import Django's built-in User model
from django.core.exceptions import ValidationError # Import used to raise validation errors in forms
from .models import Booking # Import local Booking model
import datetime # For handling date and time operations

# Form users fill in to register and sign up to the site
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

# Form users fill in to create a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["booking_date", "booking_time", "table_booked", "num_of_guests"]

    # Form validation: if a user tries to pick a booking date in the past, they'll get immediate feedback.
    def clean_booking_date(self): 
        booking_date = self.cleaned_data.get("booking_date")
        if booking_date < datetime.date.today():
            raise ValidationError("The booking date cannot be in the past. Please select another option.")
        return booking_date
        

