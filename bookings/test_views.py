from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm
import datetime

class BookingViewsTestCase(TestCase):

    def setUp(self):
        """Set up user and initial booking for testing."""
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Optionally, create a booking if it's needed for your views
        self.booking = Booking.objects.create(
            booking_date=datetime.date.today() + datetime.timedelta(days=1),
            booking_time='19:00',
            table_booked=1,
            num_of_guests=4,
            special_requests='No special requests',
            user=self.user
        )
        
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

    def test_get_booking_form(self):
        """Test the GET request for the booking form view."""
        response = self.client.get(reverse('booking_form'))  # Adjust URL name if needed
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_form.html')  # Adjust template name if needed
        self.assertIsInstance(response.context['form'], BookingForm)
        # Check that specific content is present in the response (if applicable)
        self.assertIn(b'Booking Form', response.content)  # Adjust based on actual content

    def test_post_booking_form_valid(self):
        """Test valid POST request submission for the booking form."""
        form_data = {
            'booking_date': (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        response = self.client.post(reverse('booking_form'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful submission
        # Verify the booking is saved in the database with correct data
        self.assertTrue(Booking.objects.filter(
            booking_date=form_data['booking_date'],
            booking_time=form_data['booking_time'],
            table_booked=form_data['table_booked'],
            num_of_guests=form_data['num_of_guests'],
            special_requests=form_data['special_requests'],
            user=self.user
        ).exists())

    def test_post_booking_form_invalid(self):
        """Test invalid POST request submission for the booking form."""
        form_data = {
            'booking_date': (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),  # Invalid date in the past
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        response = self.client.post(reverse('booking_form'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Expect to re-render the form on failure
        # Check for form error
        self.assertFormError(response, 'form', 'booking_date', 'The booking date cannot be in the past. Please select another date.')
