from django.shortcuts import render
from django.views import generic
from .models import Booking
from django.contrib.auth.views import LoginView  # Import Django's built-in login view


# Homepage View
class HomePage(generic.TemplateView):
    template_name = "index.html" # Do I need to change this to "home.html"?


# Sign Up Page View
class SignUpView(generic.CreateView):
    # form_class = UserCreationForm
    template_name = "sign_up.html"
    # success_url = reverse_lazy("login") # Redirects to the login page when sign up is successful


# Login View = using Django's built-in LoginView


# Booking List for Admin View
class BookingListAdmin(generic.ListView):
    model = Booking
    template_name = "bookings/bookings_list_admin.html"
    context_object_name = "bookings_list_for_admin"


# Booking List for User View
class BookingListUser(generic.ListView):
    model = Booking
    template_name = "bookings/booking_list_user.html"
    context_object_name = "booking_list_for_user"


# Make a Booking View
class BookingCreateView(generic.CreateView):
    model = Booking
    # form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = "/" # Will redirect to homepage or another page after booking




