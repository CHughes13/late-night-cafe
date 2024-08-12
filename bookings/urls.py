from . import views
from django.urls import path
from django.contrib.auth.views import LoginView  # Import Django's built-in login view

#URL pattern order should go from the least to the most specific to ensure that only one path matches.
urlpatterns = [
    # This is what is shown on the Homepage
    path("", views.BookingList.as_view(), name="home"),

    # Page where User can create a new booking
    path("create-booking/", BookingCreateView.as_view(), name="create_booking"),

    # User dashboard page where they can see their bookings
    path("dashboard/", BookingListView.as_view(), name="user_dashboard"),

    # Page where User can updating an existing booking 
     path('update-booking/<int:pk>/', BookingUpdateView.as_view(), name='update_booking'),

    # Page where User can delete an existing booking 
    path('delete-booking/<int:pk>/', BookingDeleteView.as_view(), name='delete_booking'),
]