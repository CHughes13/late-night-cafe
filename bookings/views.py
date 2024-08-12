from django.shortcuts import render, get_object_or_404 # function is a shortcut for rendering a template and returning an HTTP response
from django.views import generic # Import Django's built-in generic views
from django.contrib.auth.views import LoginView  # Import Django's built-in login view
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for sign up
from django.urls import reverse_lazy # Handles URL redirection
from .models import Booking # Import local Booking model
from .forms import CustomUserCreationForm, BookingForm #Import local CustomUserCreationForm and Booking Form

# Create your views here
# Note: for Login View = using Django's built-in LoginView

# Latte Night Cafe Homepage
class HomePageView(generic.TemplateView):
    template_name = "bookings/index.html"

 # List of all Bookings for Admin
class BookingList(generic.ListView):
    queryset = Booking.objects.all().order_by("booking_created_at")
    template_name = "bookings/index.html"
    # queryset = Booking.objects.all()
    # HELP FOR FILTERS: queryset = Post.objects.filter(https://www.w3schools.com/django/django_queryset_filter.php)

# User Dashboard
class BookingListView(generic.ListView):
    model = Booking
    template_name = "bookings/user_dashboard.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# Create a Booking Form
class BookingCreateView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("user_dashboard") # Will redirect to user dashboard

# Create or Edit a Booking
# Create or Edit a Booking
def booking_form(request, booking_id=None):
	if booking_id:
		booking = get_object_or_404(Booking, id=booking_id)
	else:
		booking = None

	if request.method == "POST":
		print("Received a POST request")
		form = BookingForm(request.POST, instance=booking)

		if form.is_valid():
			booking = form.save(commit=False) # Returns object that hasn't been saved to database yet so it can be modified further.
			booking.user = request.user
			booking.booking = booking
			booking.save()
			messages.add_message(
				request, messages.SUCCESS,
				"Booking submitted. We look forward to your visit!"
			)
			return redirect("user_dashboard") # User is returned to dashboard where they can see their booking/s
	else:
		form = BookingForm(instance=booking)

	return render(
		request,
		"bookings/booking_detail.html",
		{"form": form, "booking": booking},
	)



# Edit a Booking
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

# Booking List for Admin
class AdminBookingListView(generic.ListView):
    queryset = Booking.objects.all().order_by("booking_created_at")
    template_name = "bookings/index.html"
    context_object_name = "bookings"
    # queryset = Booking.objects.all()
    # HELP FOR FILTERS: queryset = Post.objects.filter(https://www.w3schools.com/django/django_queryset_filter.php)