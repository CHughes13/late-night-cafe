from django.shortcuts import render, get_object_or_404 # function is a shortcut for rendering a template and returning an HTTP response
from django.views import generic # Import Django's built-in generic views
from django.contrib import messages
from django.contrib.auth.views import LoginView  # Import Django's built-in login view
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for sign up
from django.urls import reverse_lazy # Handles URL redirection
from .models import Booking # Import local Booking model
from .forms import CustomUserCreationForm, BookingForm # Import local CustomUserCreationForm and Booking Form

# Create your views here
# Note: for Login View = using Django's built-in LoginView

# Latte Night Cafe Homepage
class HomePageView(generic.TemplateView):
    template_name = "bookings/index.html"

# User Dashboard
class BookingListView(generic.ListView):
    model = Booking
    template_name = "bookings/user_dashboard.html"
    context_object_name = "bookings"

    def get_queryset(self): # Filters bookings so current user can only see their own
        return Booking.objects.filter(user=self.request.user).order_by("booking_date", "booking_time") # Orders the users bookings by date then time/chronological order

# Create a Booking Form
class BookingCreateView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("user_dashboard") # Will redirect to user dashboard

def booking_form(request, booking_id=None):
    if booking_id:
        booking = get_object_or_404(Booking, id=booking_id)
    else:
        booking = None

    # This block handles the form submission
    if request.method == "POST":
        print("Received a POST request") # Prints message to console for debugging purposes
        form = BookingForm(request.POST, instance=booking) # Creates an instance of the form with the submitted data
        if form.is_valid(): # Checks if form's validation rules are met
            form.save() # Saves the form to the booking instance
            messages.add_message( # Feedback for user confirming their booking
                request, messages.SUCCESS,
                "Booking submitted. We look forward to your visit!"
            )
            return redirect("user_dashboard") # User is returned to dashboard where they can see their booking/s

    # This block handles the GET requests and displays the form
    else:
        form = BookingForm(instance=booking) # Empty form for user to fill in

    # This block renders the Template
    return render(
        request,
        "bookings/booking_detail.html",
        {"form": form, "booking": booking},
    )

# Update/Edit a Booking
class BookingUpdateView(generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/update_booking.html"
    success_url = reverse_lazy("user_dashboard") # Will redirect to user dashboard

# Delete a Booking
class BookingDeleteView(generic.DeleteView):
    model = Booking
    template_name = "bookings/confirm_delete.html"
    success_url = reverse_lazy("user_dashboard") # Will redirect to user dashboard

# List of all Bookings for Admin - DELETE if no time left to implement this
# class BookingList(generic.ListView):
#     queryset = Booking.objects.all().order_by("booking_created_at")
#     template_name = "bookings/admin_booking_list.html"
#     queryset = Booking.objects.all()
#     HELP FOR FILTERS: queryset = Post.objects.filter(https://www.w3schools.com/django/django_queryset_filter.php)
