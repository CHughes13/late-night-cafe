from django.http import Http404
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

"""
If an unauthorised user tries to access a booking that they are not the
owner of (or not a superuser/admin), they will be diverted to a 404 page.
"""

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        booking = self.get_object()

        # Allows superusers access any booking by any user
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        # Otherwise, checks to see if the booking belongs to the current user
        if booking.user != request.user:
            raise PermissionDenied("You do not have permission to edit or delete this booking.")

        return super().dispatch(request, *args, **kwargs)





#class UserIsOwnerMixin:
   # def dispatch(self, request, *args, **kwargs):
       # obj = self.get_object()
       # if obj.user != self.request.user:
           # raise Http404("You do not have permission to access this page.")
      #  return super().dispatch(request, *args, **kwargs)
