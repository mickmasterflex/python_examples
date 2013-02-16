from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.db import models

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

def permissions_required(permissions):
    def is_permitted(user):
        if not user.profile.is_permitted(permissions):
            raise PermissionDenied
        return True
    return user_passes_test(is_permitted)


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class PermissionsRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.profile.is_permitted(self.permissions_required):
            raise PermissionDenied
        return super(PermissionsRequiredMixin, self).dispatch(
            request, *args, **kwargs)

