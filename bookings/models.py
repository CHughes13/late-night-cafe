from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User model
class User(models.Model):
    (Primary Key) id (int) # Unique user id
    first_name (char) # User's first name
    last_name (char) # User's last name
    email (email) # User email address
    password (char) # User password
    is_admin (boolean) # Indicates if User is admin or not. Default set to false.


# Model for table availability info
class CafeTable(models.Model):
    (Primary Key) CafeTable id (int) # Unique table id
    num_of_seats (int) # Number of seats at a table (4 seats total)
    is_available (boolean) # Indicates if a table is avliable or not. Default set to true.


# Model for making a booking
class Booking(models.Model):
    user = models.ForeignKey(User)
    (Primary Key) Booking id (int) # Unique booking id
    (ForeignKey, User) user_id (int) # Relationship to User model
    (ForeignKey, CafeTable) CafeTable id (int) # Relationship to CafeTable model
    booking_date (date) # Date when customer wants to book table - Mon-Sun
    booking_time (time) # Time when customer wants to book table - only in 1 hour slots from 6pm-6am
    num_of_guests (int) # Number of guests must be be min 1 and max 4
    special_requests (text) # Textfield so customers can add allergy info, birthday treats, etc.
    booking_created_at = models.DateTimeField(auto_now_add=True) # Adds date & time booking was made, can't change
    booking_updated_at = models.DateTimeField(auto_now=True) # Adds date & time booking was amened, can change