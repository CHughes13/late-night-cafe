from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone # Pulls in default timezone info which is Europe/London

# Create your models here.

# Model for making a booking for an available table
class Booking(models.Model):
    
    TABLE_CHOICES = [
        ("1", "Table 1"),
        ("2", "Table 2"),
        ("3", "Table 3"),
    ]

    TIMESLOT_CHOICES = [
        ("18:00", "6 PM"),
        ("19:00", "7 PM"),
        ("20:00", "8 PM"),
        ("21:00", "9 PM"),
        ("22:00", "10 PM"),
        ("23:00", "11 PM"),
        ("00:00", "12 AM"),
        ("01:00", "1 AM"),
        ("02:00", "2 AM"),
        ("03:00", "3 AM"),
        ("04:00", "4 AM"),
        ("05:00", "5 AM"),
    ]

    NUM_GUESTS_CHOICES = [(i, i) for i in range(1, 5)] # Limits number of guests from min 1 to max 4. Futureproofing in case more tables are added with varying seat numbers.

    booking_id = models.AutoField(primary_key = True) # Unique booking id
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings') # Relationship to User model. If user is deleted, booking will be deleted too.
    table_booked = models.CharField(choices=TABLE_CHOICES, default="1") # Lists choice of tables in cafe.
    booking_date = models.DateField(null = False, blank = False) # Date when customer wants to book table - Mon-Sun. Date & time separate to allow for more flexibility for users to modify their booking. Field needs a value input. 
    booking_time = models.CharField(max_length = 6, choices=TIMESLOT_CHOICES, default="6 PM") # Lists bookable timeslots (1 hour slots from 6pm-6am).
    num_of_guests = models.IntegerField(choices=NUM_GUESTS_CHOICES, default=1) # Default number of guests is set to 1. Field needs a value input. 
    special_requests = models.TextField(null = True, blank = True) # Textfield so customers can add allergy info, birthday treats, etc. Optional field.
    booking_created_at = models.DateTimeField(auto_now_add = True) # Sets timestamp only when the record is created
    booking_updated_at = models.DateTimeField(auto_now = True) # Updates timestamp every time the record is saved

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["booking_date", "booking_time", "table_booked"] # Shows bookings in chronological order (by date, then time, then table number)
        unique_together = ["booking_date", "booking_time", "table_booked"] # Ensures that the same table can't be booked on the same date/time

    def __str__(self):
        return f"Booking for {self.user} ({self.booking_id}) at {self.table_booked} on {self.booking_date} at {self.booking_time} for {self.num_of_guests}." # Method returns a string summarising a table booking

