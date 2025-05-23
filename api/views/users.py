from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers.users import UserSerializer


class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)