from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def staff_only(f):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return f(request, *args, **kwargs)
        raise PermissionDenied
    return wrapper
