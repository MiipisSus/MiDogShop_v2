from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, extend_schema_view

from api.models import User, CustomerAddressHome
from api.serializers.users import UserSerializer, CustomerAddressHomeSerializer
from api.permissions import IsAdminUserOrOwner
from api.common import PERMMISIONS_DOCS


@extend_schema_view(
    list=extend_schema(summary=f"取得使用者清單 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增使用者 {PERMMISIONS_DOCS.NoAuth}"),
    retrieve=extend_schema(summary=f"取得使用者資料 {PERMMISIONS_DOCS.IsAuthenticated}"),
    update=extend_schema(summary=f"更新使用者資料 {PERMMISIONS_DOCS.IsAdminUserOrOwner}"),
    partial_update=extend_schema(summary=f"更新使用者資料 {PERMMISIONS_DOCS.IsAdminUserOrOwner}"),
    destroy=extend_schema(summary=f"刪除使用者資料 {PERMMISIONS_DOCS.IsAdminUserOrOwner}"),
)
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
        methods=['DELETE'],
        summary=f"刪除目前使用者資料 {PERMMISIONS_DOCS.IsAuthenticated}"
    )
    @extend_schema(
        methods=['PATCH', 'PUT'],
        summary=f"更新目前使用者資料 {PERMMISIONS_DOCS.IsAuthenticated}"
    )
    @extend_schema(
        methods=['GET'],
        summary=f"取得目前使用者資料 {PERMMISIONS_DOCS.IsAuthenticated}"
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


@extend_schema_view(
    list=extend_schema(summary=f"取得使用者地址清單 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增使用者地址 {PERMMISIONS_DOCS.IsAdminUser}"),
    retrieve=extend_schema(summary=f"取得使用者地址資料 {PERMMISIONS_DOCS.IsAuthenticated}"),
    update=extend_schema(summary=f"更新使用者地址資料 {PERMMISIONS_DOCS.IsAdminUserOrOwner}"),
    partial_update=extend_schema(summary=f"更新使用者地址資料 {PERMMISIONS_DOCS.IsAdminUserOrOwner}"),
    destroy=extend_schema(summary=f"刪除使用者地址資料 {PERMMISIONS_DOCS.IsAdminUserOrOwner}"),
)
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
    
