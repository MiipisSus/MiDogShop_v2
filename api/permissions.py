from rest_framework.permissions import BasePermission, SAFE_METHODS

from api.models import CustomerAddressHome, Order, User
    
    
class IsStaff(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user and user.is_authenticated and (
                user.is_superuser or
                user.groups.filter(name__in=['Staff', 'Manager']).exists()
            )
        )


class IsManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user and user.is_authenticated and (
                user.is_superuser or
                user.groups.filter(name='Manager').exists()
            )
        )