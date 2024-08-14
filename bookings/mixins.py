from django.http import Http404
from django.contrib.auth.mixins import UserPassesTestMixin


"""
If an unauthorised user tries to access a booking that they are not the
owner of, they will be diverted to a 404 page
"""

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise Http404("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)


# Checks to see if user is superuser
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
        