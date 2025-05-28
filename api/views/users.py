from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, extend_schema_view

from api.models import User, CustomerAddressHome
from api.serializers.users import UserSerializer, CustomerAddressHomeSerializer
from api.permissions import IsAdminUserOrOwner


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUserOrOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(groups__name='Customer')

    def get_permissions(self):
        if self.action == 'create':
            return []
        elif self.action == 'retrieve':
            return [IsAuthenticated()]
        return super().get_permissions()
    
    @extend_schema(
        summary="新增使用者（無須權限）"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        methods=['DELETE'],
        summary="刪除目前使用者資料"
    )
    @extend_schema(
        methods=['PATCH', 'PUT'],
        summary="更新目前使用者資料"
    )
    @extend_schema(
        methods=['GET'],
        summary="取得目前使用者資料"
    )
    @action(
        detail=False, methods=['get', 'patch', 'put', 'delete'],
        url_path='me', permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        self.kwargs[self.lookup_field] = user.pk

        if request.method == 'GET':
            return self.retrieve(request)
        elif request.method in ['PATCH', 'PUT']:
            return self.partial_update(request) if request.method == 'PATCH' else self.update(request)
        elif request.method == 'DELETE':
            return self.destroy(request)


class CustomerAddressHomeViewSet(ModelViewSet):
    queryset = CustomerAddressHome.objects.all()
    serializer_class = CustomerAddressHomeSerializer
    permission_classes = [IsAdminUserOrOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomerAddressHome.objects.all()
        return super().get_queryset().filter(customer=self.request.user)
    
    @action(detail=False, methods=['get', 'post'],
            url_path='me', permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        self.kwargs[self.lookup_field] = user.pk
        
        if request.method == 'GET':
            return self.list(request)
        elif request.method == 'POST':
            request.data['customer'] = user.pk
            return self.create(request)
        
    def update(self, request, *args, **kwargs):
        # prevent the customer_id to be changed
        request.data['customer'] = self.request.user.pk
        return super().update(request, *args, **kwargs)
    
