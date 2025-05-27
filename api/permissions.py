from rest_framework.permissions import BasePermission, SAFE_METHODS

from api.models import CustomerAddressHome, Order, User


def check_object_owner(obj, user):
    if isinstance(obj, CustomerAddressHome) or isinstance(obj, Order):
        return obj.customer == user
    elif isinstance(obj, User):
        return obj == user
    else:
        return False


class IsOwner(BasePermission):
    """
    只允許物件的擁有者編輯它
    """
    def has_object_permission(self, request, view, obj):
        # Add any model check if needed
        return check_object_owner(obj, request.user)


class IsAdminUserOrOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        # Create methods only available to staff. If the user is not staff, they should use /me endpoint
        elif request.method == 'POST':
            return bool(request.user and request.user.is_staff)
        else:
            return True
    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user.is_staff or check_object_owner(obj, request.user)))
