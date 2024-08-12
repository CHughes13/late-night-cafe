from . import views
from django.urls import path
from django.contrib.auth.views import LoginView  # Import Django's built-in login view

#URL pattern order should go from the least to the most specific to ensure that only one path matches.
urlpatterns = [
    # This is what is shown on the Homepage
    path("", views.BookingList.as_view(), name="home"),

    # Create booking page
    path("create-booking/", views.create_booking, name="create_booking"),

    # User dashboard page that is seen why user logs in
    path('dashboard/', views.user_dashboard, name='user_dashboard'),

    # Update booking page
    path('update-booking/<int:booking_id>/', views.update_booking, name='update_booking'),

    # Delete booking page
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]