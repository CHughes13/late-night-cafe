from django.contrib import admin
from .models import Booking
from .forms import CustomUserCreationForm

# Register Booking model with default admin interface
admin.site.register(Booking)