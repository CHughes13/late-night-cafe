from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # Pulls in default timezone info which is Europe/London

# Create your models here.

# User model
class User(models.Model):
    id = models.AutoField(primary_key = True) # Unique User id
    first_name = models.CharField(max_length = 50) # User's first name, allows a max length of 50 characters 
    last_name = models.CharField(max_length = 50) # User's last name, allows a max length of 50 characters 
    email = models.EmailField(unique = True, max_length = 254) # Ensures User email address is used just once on the site & not too long
    password = models.CharField(max_length=128) # User password
    is_admin = models.BooleanField(default=False) # Indicates if User is admin or not. Default set to false.


# Model for table availability info
class CafeTable(models.Model):
    id = models.AutoField(primary_key = True) # Unique table id
    num_of_seats = models.PositiveSmallIntegerField() # Number of seats at a table (4 seats total).
    #potentially add (validators=[MinValueValidator(0)]) at the end as field cannot be negative, but 0 would be allowed.
   
    is_available = models.BooleanField(default=True) # Indicates if a table is available or not. Default set to true.
   


# Model for making a booking
class Booking(models.Model):
    id = models.AutoField(primary_key = True) # Unique booking id
    user = models.ForeignKey(User) # Relationship to User model
    table_booked = models.ForeignKey(CafeTable) # Relationship to CafeTable model
    booking_date = models.DateField() # Date when customer wants to book table - Mon-Sun. Date & time seperate to allow for more flexibility for users to modify their booking.
    booking_time = models.TimeField() # Time when customer wants to book table - only in 1 hour slots from 6pm-6am
    num_of_guests = models.IntegerField() # Number of guests must be be min 1 and max 4
    special_requests = models.TextField() # Textfield so customers can add allergy info, birthday treats, etc.
    booking_created_at = models.DateTimeField(auto_now_add=True, default=timezone.now) # Adds Europe/London date & time booking was first made, can't be changed
    booking_updated_at = models.DateTimeField(auto_now=True, default=timezone.now) # Adds Europe/London date & time booking was amened, can be changed