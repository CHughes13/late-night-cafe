from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # Pulls in default timezone info which is Europe/London

# Create your models here.

# User model
class User(models.Model):
    id = models.AutoField(primary_key = True) # Unique User id
    first_name = models.CharField(max_length = 50, null = False, blank = False) # User's first name, allows a max length of 50 characters. Field needs a value input. 
    last_name = models.CharField(max_length = 50, null = False, blank = False) # User's last name, allows a max length of 50 characters. Field needs a value input. 
    email = models.EmailField(unique = True, max_length = 254, null = False, blank = False) # Ensures User email address is used just once on the site & not too long. Field needs a value input. 
    password = models.CharField(max_length = 128, null = False, blank = False) # User password. Field needs a value input. 
    is_admin = models.BooleanField(default = False) # Indicates if User is admin or not. Default set to false.


# Model for table availability info
class CafeTable(models.Model):
    id = models.AutoField(primary_key = True) # Unique table id
    num_of_seats = models.PositiveSmallIntegerField(null = False, blank = False) # Number of seats at a table (4 seats total). Field needs a value input. 
    #potentially add (validators=[MinValueValidator(0)]) at the end as field cannot be negative, but 0 would be allowed.
   
    is_available = models.BooleanField(default = True) # Indicates if a table is available or not. Default set to true.
   


# Model for making a booking
class Booking(models.Model):
    id = models.AutoField(primary_key = True) # Unique booking id
    user = models.ForeignKey(User) # Relationship to User model
    table_booked = models.ForeignKey(CafeTable) # Relationship to CafeTable model
    booking_date = models.DateField(null = False, blank = False) # Date when customer wants to book table - Mon-Sun. Date & time seperate to allow for more flexibility for users to modify their booking. Field needs a value input. 
    booking_time = models.TimeField(null = False, blank = False) # Time when customer wants to book table - only in 1 hour slots from 6pm-6am. Field needs a value input.
    NUM_GUESTS_CHOICES = [(i, i) for i in range(1, 5)] # Limits number of guests from min 1 to max 4
    num_of_guests = models.IntegerField(choices=NUM_GUESTS_CHOICES, default=1) # Default number of guests is set to 1. Field needs a value input. 
    special_requests = models.TextField(null = True, blank = True) # Textfield so customers can add allergy info, birthday treats, etc. Optional field.
    booking_created_at = models.DateTimeField(auto_now_add = True, default=timezone.now) # Adds Europe/London date & time booking was first made, can't be changed
    booking_updated_at = models.DateTimeField(auto_now = True, default=timezone.now) # Adds Europe/London date & time booking was amened, can be changed