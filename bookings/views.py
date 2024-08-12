from django.shortcuts import render, get_object_or_404 # function is a shortcut for rendering a template and returning an HTTP response
from django.views import generic # Import Django's built-in generic views
from django.contrib.auth.views import LoginView  # Import Django's built-in login view
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for sign up
from django.urls import reverse_lazy # Handles URL redirection
from .models import Booking # Import local Booking model
from .forms import CustomUserCreationForm, BookingForm #Import local CustomUserCreationForm and Booking Form

# Create your views here
# Note, for Login View = using Django's built-in LoginView

class BookingList(generic.ListView):
    queryset = Booking.objects.all().order_by("booking_created_at")
    template_name = "bookings/index.html"
    # queryset = Booking.objects.all()
    # HELP FOR FILTERS: queryset = Post.objects.filter(https://www.w3schools.com/django/django_queryset_filter.php)

# Make a Booking View
class BookingCreateView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("user_dashboard") # Will redirect to homepage or another page after booking

# User Dashboard
class BookingListView(generic.ListView):
    model = Booking
    template_name = "bookings/user_dashboard.html"
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# Edit a Booking
class BookingUpdateView(generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/update_booking.html"
    success_url = reverse_lazy("user_dashboard")

# Delete a Booking
class BookingDeleteView(generic.DeleteView):
    model = Booking
    template_name = 'bookings/confirm_delete.html'
    success_url = reverse_lazy('user_dashboard')