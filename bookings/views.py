from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

def my_bookings(request):
    return HttpResponse("Hello World!")