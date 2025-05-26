from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

from api.models import User, CustomerAddressHome
from api.serializers.users import UserSerializer, CustomerAddressHomeSerializer
from api.permissions import IsOwnerOrReadOnly

class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsOwnerOrReadOnly]
  
  def get_queryset(self):
    if self.request.user.is_staff:
      return User.objects.all()
    return super().get_queryset().filter(groups__name='Customer')


class CustomerAddressHomeViewSet(ModelViewSet):
  queryset = CustomerAddressHome.objects.all()
  serializer_class = CustomerAddressHomeSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    if self.request.user.is_staff:
      return CustomerAddressHome.objects.all()
    return super().get_queryset().filter(customer=self.request.user)