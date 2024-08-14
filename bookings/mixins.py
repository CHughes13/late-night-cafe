from django.http import Http404

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