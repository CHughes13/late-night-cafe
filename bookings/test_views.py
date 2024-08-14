from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm

class TestBookingViews(TestCase):

    def setUp(self):
        """Set up user and booking for testing."""
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

    def test_render_booking_page(self):
        """Test the booking page view."""
        response = self.client.get(reverse('booking_form'))  # Adjust URL name if needed
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_form.html')  # Adjust template name if needed
        self.assertIsInstance(response.context['form'], BookingForm)
        # You can also test for specific content in the response
        self.assertIn(b'Booking Form', response.content)  # Adjust based on actual content

    def test_booking_form_valid_submission(self):
        """Test valid form submission."""
        form_data = {
            'booking_date': datetime.date.today() + datetime.timedelta(days=1),
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        response = self.client.post(reverse('booking_form'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful submission
        self.assertTrue(Booking.objects.filter(user=self.user).exists())

    def test_booking_form_invalid_submission(self):
        """Test invalid form submission."""
        form_data = {
            'booking_date': datetime.date.today() - datetime.timedelta(days=1),  # Invalid date in the past
            'booking_time': '19:00',
            'table_booked': 1,
            'num_of_guests': 4,
            'special_requests': 'No special requests',
        }
        response = self.client.post(reverse('booking_form'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Expect to re-render the form on failure
        self.assertFormError(response, 'form', 'booking_date', 'The booking date cannot be in the past. Please select another date.')

