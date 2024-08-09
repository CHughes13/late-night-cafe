from django.contrib import admin
from django.contrib.auth.models import User
from .models import Booking
from .forms import CustomUserCreationForm

# Register Booking model with default admin interface
admin.site.register(Booking)

# Register Django's default User model
admin.site.register(User)