from rest_framework.permissions import BasePermission, SAFE_METHODS

from api.models import CustomerAddressHome, Order, User

class IsOwnerOrReadOnly(BasePermission):
    """
    只允許物件的擁有者編輯它
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
          
        # Add any model check if needed
        if isinstance(obj, CustomerAddressHome) or isinstance(obj, Order):
          return obj.customer == request.user
        elif isinstance(obj, User):
          return obj == request.user
        else:
          return False