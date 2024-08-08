from django import forms
from django.contrib.auth.forms import UserCreationForm # Import Django's built-in UserCreationForm
from django.contrib.auth.models import User # Import Django's built-in User
from .models import Booking # Import local Booking model

# Form users fill in to register and sign up to the site
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

# Form users fill in to create a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["booking date", "booking_time", "table_booked"]