from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # Pulls in default timezone info which is Europe/London

# Create your models here.


# Model for table availability info
class CafeTable(models.Model):
    cafe_table_id = models.AutoField(primary_key = True) # Unique table id
    is_available = models.BooleanField(default = True) # Indicates if a table is available or not. Default set to true.

    """
    Commenting out - all tables have 4 seats for simplicity. Future feature could incorporate variying seat numbers
    num_of_seats = models.PositiveSmallIntegerField(null = False, blank = False) # Number of seats at a table (4 seats total). Field needs a value input. 
    #potentially add (validators=[MinValueValidator(0)]) at the end as field cannot be negative, but 0 would be allowed.
   """
    def __str__(self):
        return f"Table {self.cafe_table_id} {'is available' if self.is_available else 'is not available'}" # Method returns a string showing if a table is available or not



# Model for making a booking
class Booking(models.Model):
    booking_id = models.AutoField(primary_key = True) # Unique booking id
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings') # Relationship to User model. If user is deleted, booking will be deleted too.
    table_booked = models.ForeignKey(CafeTable, on_delete=models.CASCADE, related_name='bookings') # Relationship to CafeTable model. If table is deleted, so will all bookings associated with that table.
    booking_date = models.DateField(null = False, blank = False) # Date when customer wants to book table - Mon-Sun. Date & time separate to allow for more flexibility for users to modify their booking. Field needs a value input. 
    booking_time = models.TimeField(null = False, blank = False) # Time when customer wants to book table - only in 1 hour slots from 6pm-6am. Field needs a value input.
    NUM_GUESTS_CHOICES = [(i, i) for i in range(1, 5)] # Limits number of guests from min 1 to max 4
    num_of_guests = models.IntegerField(choices=NUM_GUESTS_CHOICES, default=1) # Default number of guests is set to 1. Field needs a value input. 
    special_requests = models.TextField(null = True, blank = True) # Textfield so customers can add allergy info, birthday treats, etc. Optional field.
    booking_created_at = models.DateTimeField(auto_now_add = True) # Sets timestamp only when the record is created
    booking_updated_at = models.DateTimeField(auto_now = True) # Updates timestamp every time the record is saved

    def __str__(self):
        return f"Booking for {self.user} ({self.booking_id}) on {self.booking_date} at {self.booking_time} for {self.num_of_guests}." # Method returns a string summarising a table booking