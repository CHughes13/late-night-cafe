from . import views
from django.urls import path
from django.contrib.auth.views import LoginView  # Import Django's built-in login view

# URL pattern order should go from the least to the most specific to ensure that only one path matches.

urlpatterns = [

    # This is what is shown on the Homepage test
    path("", views.HomePageView.as_view(), name="home"),

    # Page where User can create a new booking
    path("create-booking/", views.BookingCreateView.as_view(), name="create_booking"),

    # User dashboard page where they can see all their bookings
    path("dashboard/", views.BookingListView.as_view(), name="user_dashboard"),

    # So User can update an existing booking
    path("update-booking/<int:pk>/", views.BookingUpdateView.as_view(), name="update_booking"),

    # So User can delete an existing booking
    path("delete-booking/<int:pk>/", views.BookingDeleteView.as_view(), name="delete_booking"),

    # List of all Bookings just for admin
    #path("admin-booking-list/", views.AdminBookingListView.as_view(), name="admin_booking_list"),
]