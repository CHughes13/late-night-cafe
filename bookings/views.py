from django.shortcuts import render, get_object_or_404
from django.views import generic # Import Django's built-in generic views
from django.contrib.auth.views import LoginView  # Import Django's built-in login view
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for sign up
from django.urls import reverse_lazy # Handles URL redirection
from .models import Booking # Import local Booking model
from .forms import CustomUserCreationForm, BookingForm #Import local CustomUserCreationForm and Booking Form
from django.shortcuts import render # function is a shortcut for rendering a template and returning an HTTP response

# Create your views here

class BookingList(generic.ListView):
    # queryset = Booking.objects.all()
    template_name = "bookings/booking_list.html"
    # HELP FOR FILTERS: queryset = Post.objects.filter(https://www.w3schools.com/django/django_queryset_filter.php)
    queryset = Booking.objects.all().order_by("-booking_created_at")

# Homepage View
#class HomePage(generic.TemplateView):
    #template_name = "bookings/index.html" # Path to index template


# Sign Up Page View
#class SignUpView(generic.CreateView):
   # form_class = CustomUserCreationForm
   # template_name = "sign_up.html"
   # success_url = reverse_lazy("login") # Redirects to the login page when sign up is successful


# Login View = using Django's built-in LoginView


# Booking List for Admin View
#class BookingListAdmin(generic.ListView):
   # model = Booking
    #template_name = "bookings/bookings_list_admin.html"
    #context_object_name = "bookings_list_for_admin"


# Booking List for User View
#class BookingListUser(generic.ListView):
    #model = Booking
    #template_name = "bookings/booking_list_user.html"
    #context_object_name = "booking_list_for_user"


# Make a Booking View
#class BookingCreateView(generic.CreateView):
    #model = Booking
   # form_class = BookingForm
   # template_name = "bookings/booking_form.html"
   # success_url = "/" # Will redirect to homepage or another page after booking




