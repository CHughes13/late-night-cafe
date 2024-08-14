from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

"""
If an unauthorised user tries to access a booking that they are not the
owner of (or not a superuser/admin), they will be diverted to a 404 page.
"""

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return self.redirect_to_login()



class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        booking = self.get_object()

        # Allow superusers to access any booking
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        # Ensure that only the owner can access the booking
        if booking.user != request.user:
            raise PermissionDenied("You do not have permission to edit or delete this booking.")

        return super().dispatch(request, *args, **kwargs)
