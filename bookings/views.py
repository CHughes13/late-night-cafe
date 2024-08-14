from django.shortcuts import render, get_object_or_404, reverse # function is a shortcut for rendering a template and returning an HTTP response
from django.views import generic # Import Django's built-in generic views
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView  # Import Django's built-in login view
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for sign up
from django.urls import reverse_lazy # Handles URL redirection
from .models import Booking # Import local Booking model
from .forms import CustomUserCreationForm, BookingForm # Import local CustomUserCreationForm and Booking Form
from .mixins import UserIsOwnerMixin, SuperuserRequiredMixin # Import mixins.py
from django.shortcuts import redirect


# Note: for Login View = using Django's built-in LoginView

# GENERAL VIEWS
# Latte Night Cafe Homepage
class HomePageView(generic.TemplateView):
    template_name = "bookings/index.html"


# ADMIN VIEWS

# Admin Dashboard - lists bookings for all users for the logged-in site admin

class AdminBookingListView(SuperuserRequiredMixin, generic.ListView): # Admin = Superuser for now, can expand permissions to staff Admin when business expands
    model = Booking
    template_name = "bookings/admin_dashboard.html"
    context_object_name = "bookings"
    success_url = reverse_lazy("admin_dashboard")

    def get_queryset(self): 
        queryset = Booking.objects.all() # Filters bookings so Admin can see all bookings

        # Ability to sort bookings
        sort_by = self.request.GET.get('sort_by', 'booking_date')  # Default sort by booking date
        sort_order = self.request.GET.get('sort_order', 'asc')     # Default sort order is ascending

        if sort_order == 'desc': # If sort order is descending
            sort_by = f'-{sort_by}'

        queryset = queryset.order_by(sort_by)

        return queryset


def booking_form(request, booking_id=None):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "You need to be logged in to create a booking.")
        return redirect(reverse("account_login"))

    if booking_id: # Checks to see if booking_id is provided
        booking = get_object_or_404(Booking, id=booking_id) # If there is a booking id, then the form will populate with data from that existing booking
    else:
        booking = None # If there is no booking id, then the form will be blank and new

    # This block handles the form submission
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        
        if form.is_valid(): # Checks if form's validation rules are met
            booking = form.save(commit=False)  # Doesn't commit form to the database yet
            booking.user = request.user  # Assigns the logged-in user to the booking
            booking.save()  # Now saves form to the database
            messages.add_message(request, messages.SUCCESS, "Booking successfully created.")
            return redirect("admin_dashboard") # Redirects back to Admin Dashboard
   
   # This block handles the GET requests and displays the form
    else:
        form = BookingForm(instance=booking) # Empty form for user to fill in
 
    # This block renders the form template
    return render(
        request,
        "bookings/booking_form.html",
        {"form": form, "booking": booking}
    )



# USER VIEWS
# User Dashboard - lists bookings for the logged in user
class BookingListView(generic.ListView):
    model = Booking
    template_name = "bookings/user_dashboard.html"
    context_object_name = "bookings"

    def get_queryset(self): # Ability to sort bookings

        queryset = Booking.objects.filter(user=self.request.user) # Filters bookings so current user can only see their own
        sort_by = self.request.GET.get('sort_by', 'booking_date')  # Default sort by booking date 
        sort_order = self.request.GET.get('sort_order', 'asc')     # Default sort order is ascending 

        if sort_order == 'desc': # If sort order is descending
            sort_by = f'-{sort_by}'

        queryset = queryset.order_by(sort_by)

        return queryset


# Create a Booking Form
class BookingCreateView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("user_dashboard") # Will redirect to user dashboard

def booking_form(request, booking_id=None):
    if not request.user.is_authenticated:
        messages.add_message( # Feedback for user letting them know they have to sign in to make a booking
                request, messages.ERROR,
                "You need to be logged in to create a booking."
        )
        return redirect(reverse("account_login")) # Redirects a non-logged in User to sign in page so they can log in/sign up so they can make a booking

    if booking_id: # Checks to see if booking_id is provided
        booking = get_object_or_404(Booking, id=booking_id) # If there is a booking id, then the form will populate with data from that existing booking
    else:
        booking = None # If there is no booking id, then the form will be blank and new
    

    # This block handles the form submission
    if request.method == "POST":
        print("Received a POST request") # Prints message to console for debugging purposes
        form = BookingForm(request.POST, instance=booking) # Creates an instance of the form with the submitted data
        
        if form.is_valid(): # Checks if form's validation rules are met
            booking = form.save(commit=False)  # Doesn't commit form to the database yet
            booking.user = request.user  # Assigns the logged-in user to the booking
            booking.save()  # Now saves form to the database
            messages.add_message( # Feedback for user confirming their booking
                request, messages.SUCCESS,
                "Booking submitted. We look forward to your visit!"
            )
            return redirect("user_dashboard") # User is returned to dashboard where they can see their booking/s

    # This block handles the GET requests and displays the form
    else:
        form = BookingForm(instance=booking) # Empty form for user to fill in

    # This block renders the form template
    return render(
        request,
        "bookings/booking_form.html",
        {"form": form, "booking": booking},
    )

# Update/Edit a Booking
class BookingUpdateView(UserIsOwnerMixin, generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/update_booking.html"

    def get_success_url(self): # if it's the admin/superuser making the booking amend they will be redirected back to the Admin Dashboard
        if self.request.user.is_superuser:
            return reverse_lazy("admin_dashboard")
        return reverse_lazy("user_dashboard")

    def form_valid(self, form):
        try:
            response = super().form_valid(form) # Saves the form/updated data to the database
            messages.success(self.request, "Your booking has been updated!")  # Sends success feedback to user
            return response
        except Exception as e: # If an error occurs during form processing then this block of code will trigger
            messages.error(self.request, "Oops! There was a problem updating your booking. Please try again.")  # Sends error feedback to user
            return self.form_invalid(form)

    def form_invalid(self, form): # Handles the error
        # This will re-render the form with error messages so the user can correct their booking details
        messages.error(self.request, "Whoops! There was an issue updating your booking. Please check your booking details and try again.")
        return super().form_invalid(form)

# Delete a Booking
class BookingDeleteView(UserIsOwnerMixin, generic.DeleteView):
    model = Booking
    template_name = "bookings/confirm_delete.html"
    success_url = reverse_lazy("user_dashboard") # Will redirect to user dashboard

    def get_success_url(self): # if it's the admin/superuser making the booking amend they will be redirected back to the Admin Dashboard
        if self.request.user.is_superuser:
            return reverse_lazy("admin_dashboard")
        return reverse_lazy("user_dashboard")

    def delete(self, request, *args, **kwargs): #This calls the parent class's delete method, which handles the deletion of the object.
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Your booking has been deleted!")  # Feedback for user that confirms their booking has been delete
        return response


