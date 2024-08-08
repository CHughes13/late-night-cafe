from django.shortcuts import render
from django.views import generic
from .models import Booking

"""
from django.views.generic import TemplateView use this when creating the HOMEPAGE
class HomePage(TemplateView):
    # "Displays home page"
    template_name = 'index.html'
"""
class BookingsListAdmin(generic.ListView):
    model = Booking
    template_name = "bookings/bookings_list_admin.html"
    context_object_name = "bookings_list_for_admin"


