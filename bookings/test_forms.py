from django.test import TestCase
from django.contrib.auth.models import User
from .forms import BookingForm
from .models import Booking
import datetime

class TestBookingForm(TestCase):

    def setUp(self):
        """Set up a test user."""
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_form_is_valid(self):
        """Test that the form is valid with correct data."""
        form_data = {
            'booking_date': datetime.date.today() + datetime.timedelta(days=1),  # Tomorrow's date
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid(), msg="Form should be valid with correct data")

    def test_booking_date_in_past(self):
        """Test that the form is invalid if booking date is in the past."""
        form_data = {
            'booking_date': datetime.date.today() - datetime.timedelta(days=1),  # Yesterday's date
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form should be invalid with a past booking date")
        self.assertIn('booking_date', form.errors, msg="Booking date should raise a validation error")

    def test_booking_date_too_far_in_future(self):
        """Test that the form is invalid if booking date is more than one year in advance."""
        form_data = {
            'booking_date': datetime.date.today() + datetime.timedelta(days=366),  # Date more than one year ahead
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form should be invalid with a booking date more than one year in advance")
        self.assertIn('booking_date', form.errors, msg="Booking date should raise a validation error")

    def test_form_is_invalid_missing_field(self):
        """Test that the form is invalid if required fields are missing."""
        form_data = {
            'booking_date': datetime.date.today() + datetime.timedelta(days=1),
            'booking_time': '',  # Missing booking time
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form should be invalid with missing booking time")
        self.assertIn('booking_time', form.errors, msg="Booking time should be required")

    def test_form_save_method(self):
        """Test that the form's save method correctly saves the booking."""
        form_data = {
            'booking_date': datetime.date.today() + datetime.timedelta(days=1),
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        form = BookingForm(data=form_data)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = self.user
            booking.save()
            self.assertTrue(Booking.objects.filter(user=self.user).exists(), msg="Booking should be saved to the database")
