from . import views
from django.urls import path
from django.contrib.auth.views import LoginView  # Import Django's built-in login view


urlpatterns = [
    # Homepage
    path("", views.HomePage.as_view(), name="home"),

    # Sign Up Page
    path("sign_up/", views.SignUpView.as_view(), name="sign_up"),

    # Login Page
    path("login/", LoginView.as_view(template_name = "registration/login.html"), name = "login" ),

    # Booking List for Admin Page
    path("admin/bookings/", views.BookingListAdmin.as_view(), name = "admin_bookings"),

    # Booking List for User Page
    path("user/bookings/", views.BookingListUser.as_view(), name = "user_bookings"),

    # Make a Booking Page
    path("make_a_booking/", views.BookingCreateView.as_view(), name = "make_a_booking"),
]