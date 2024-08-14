from django import forms
from django.contrib.auth.forms import UserCreationForm  # Import Django's built-in UserCreationForm
from django.contrib.auth.models import User  # Import Django's built-in User model
from django.core.exceptions import ValidationError  # Import used to raise validation errors in forms
from .models import Booking  # Import local Booking model
import datetime  # For handling date and time operations

# Form users fill in to register and sign up to the site
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

# Form users fill in to create a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["booking_date", "booking_time", "table_booked", "num_of_guests", "special_requests"]

    # Form validation: if a user tries to pick an invalid booking date, they'll get immediate feedback
    def clean_booking_date(self):
        booking_date = self.cleaned_data.get("booking_date")
        today = datetime.date.today()
        one_year_from_now = today + datetime.timedelta(days=365)

        # Check if the booking date is in the past
        if booking_date < today:
            raise ValidationError("The booking date cannot be in the past. Please select another date.")
        
        # Check if the booking date is more than one year in advance
        if booking_date > one_year_from_now:
            raise ValidationError("Sorry, we don't accept bookings more than one year in advance. Please select another date.")
        
        return booking_date
