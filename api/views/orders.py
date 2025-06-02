from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, SAFE_METHODS
from drf_spectacular.utils import extend_schema, extend_schema_view

from api.models import Order, OrderItem, OrderShipping, OrderAddressHome, ShippingMethod, PaymentMethod
from api.serializers import ShippingMethodSerializer, PaymentMethodSerializer, OrderSerializer, OrderItemSerializer, OrderShippingSerializer, \
    OrderAddressHomeSerializer
from api.permissions import IsStaff, IsManager, IsAdminUserOrOwner
from api.common import PERMMISIONS_DOCS


@extend_schema_view(
    list=extend_schema(summary=f"取得所有運送方式 {PERMMISIONS_DOCS.IsAuthenticated}"),
    retrieve=extend_schema(summary=f"取得運送方式 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增運送方式 {PERMMISIONS_DOCS.IsManager}"),
    update=extend_schema(summary=f"更新運送方式 {PERMMISIONS_DOCS.IsManager}"),
    partial_update=extend_schema(summary=f"更新運送方式 {PERMMISIONS_DOCS.IsManager}"),
    destroy=extend_schema(summary=f"刪除運送方式 {PERMMISIONS_DOCS.IsManager}")
)
class ShippingMethodViewSet(ModelViewSet):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer
    permission_classes = [IsManager]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return super().get_permissions()
    

@extend_schema_view(
    list=extend_schema(summary=f"取得所有付款方式 {PERMMISIONS_DOCS.IsAuthenticated}"),
    retrieve=extend_schema(summary=f"取得付款方式 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增付款方式 {PERMMISIONS_DOCS.IsManager}"),
    update=extend_schema(summary=f"更新付款方式 {PERMMISIONS_DOCS.IsManager}"),
    partial_update=extend_schema(summary=f"更新付款方式 {PERMMISIONS_DOCS.IsManager}"),
    destroy=extend_schema(summary=f"刪除付款方式 {PERMMISIONS_DOCS.IsManager}")
)
class PaymentMethodViewSet(ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsManager]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return super().get_permissions()
    

@extend_schema_view(
    list=extend_schema(summary=f"取得所有訂單 {PERMMISIONS_DOCS.IsAuthenticated}"),
    retrieve=extend_schema(summary=f"取得訂單 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增訂單 {PERMMISIONS_DOCS.IsAuthenticated}"),
    update=extend_schema(summary=f"更新訂單 {PERMMISIONS_DOCS.IsStaff}"),
    partial_update=extend_schema(summary=f"更新訂單 {PERMMISIONS_DOCS.IsStaff}"),
    destroy=extend_schema(summary=f"刪除訂單 {PERMMISIONS_DOCS.IsStaff}")
)
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsStaff]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(customer=self.request.user)
    
    def get_permissions(self):
            if self.request.method in SAFE_METHODS:
                return [IsAuthenticated()]
            elif self.request.method == 'POST':
                return [IsAuthenticated()]
            return super().get_permissions()
    

@extend_schema_view(
    list=extend_schema(summary=f"取得所有訂單項目 {PERMMISIONS_DOCS.IsAuthenticated}"),
    retrieve=extend_schema(summary=f"取得訂單項目 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增訂單項目 {PERMMISIONS_DOCS.IsAuthenticated}"),
    update=extend_schema(summary=f"更新訂單項目 {PERMMISIONS_DOCS.IsStaff}"),
    partial_update=extend_schema(summary=f"更新訂單項目 {PERMMISIONS_DOCS.IsStaff}"),
    destroy=extend_schema(summary=f"刪除訂單項目 {PERMMISIONS_DOCS.IsStaff}")
)
class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsStaff]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(order__customer=self.request.user)
    
    def get_permissions(self):
            if self.request.method in (*SAFE_METHODS, 'POST'):
                return [IsAuthenticated()]
            return super().get_permissions()
    

@extend_schema_view(
    list=extend_schema(summary=f"取得所有訂單運送方式 {PERMMISIONS_DOCS.IsAuthenticated}"),
    retrieve=extend_schema(summary=f"取得訂單運送方式 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增訂單運送方式 {PERMMISIONS_DOCS.IsAuthenticated}"),
    update=extend_schema(summary=f"更新訂單運送方式 {PERMMISIONS_DOCS.IsStaff}"),
    partial_update=extend_schema(summary=f"更新訂單運送方式 {PERMMISIONS_DOCS.IsStaff}"),
    destroy=extend_schema(summary=f"刪除訂單運送方式 {PERMMISIONS_DOCS.IsStaff}")
)
class OrderShippingViewSet(ModelViewSet):
    queryset = OrderShipping.objects.all()
    serializer_class = OrderShippingSerializer
    permission_classes = [IsStaff]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(order__customer=self.request.user)
    
    def get_permissions(self):
            if self.request.method in (*SAFE_METHODS, 'POST'):
                return [IsAuthenticated()]
            return super().get_permissions()


@extend_schema_view(
    list=extend_schema(summary=f"取得所有訂單地址 {PERMMISIONS_DOCS.IsAuthenticated}"),
    retrieve=extend_schema(summary=f"取得訂單地址 {PERMMISIONS_DOCS.IsAuthenticated}"),
    create=extend_schema(summary=f"新增訂單地址 {PERMMISIONS_DOCS.IsAuthenticated}"),
    update=extend_schema(summary=f"更新訂單地址 {PERMMISIONS_DOCS.IsStaff}"),
    partial_update=extend_schema(summary=f"更新訂單地址 {PERMMISIONS_DOCS.IsStaff}"),
    destroy=extend_schema(summary=f"刪除訂單地址 {PERMMISIONS_DOCS.IsStaff}")
)
class OrderAddressHomeViewSet(ModelViewSet):
    queryset = OrderAddressHome.objects.all()
    serializer_class = OrderAddressHomeSerializer
    permission_classes = [IsStaff]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(order__customer=self.request.user)
    
    def get_permissions(self):
        if self.request.method in (*SAFE_METHODS, 'POST'):
            return [IsAuthenticated()]
        return super().get_permissions()
