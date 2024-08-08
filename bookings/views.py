from django.shortcuts import render
from django.views import generic
from .models import Booking


# Homepage view
class HomePage(generic.TemplateView):
    template_name = "index.html" # Do I need to change this to "home.html"?


# Sign Up Page view
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "sign_up.html"
    success_url = reverse_lazy("login") # Redirects to the login page when sign up is successful

# Login view
# Django's built-in LoginView is used directly in urls.py


# Bookings List for Admin view
class BookingsListAdmin(generic.ListView):
    model = Booking
    template_name = "bookings/bookings_list_admin.html"
    context_object_name = "bookings_list_for_admin"

# Bookings List for User view
class BookingsListUser(generic.ListView):
    model = Booking
    template_name = "bookings/booking_list_user.html"
    context_object_name = "booking_list_for_user"

# Make a Bookings view
class BookingCreateView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = "/" # Will redirect to homepage or another page after booking




