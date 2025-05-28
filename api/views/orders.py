from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, SAFE_METHODS

from api.models import Order, OrderItem, OrderShipping, OrderAddressHome, ShippingMethod, PaymentMethod
from api.serializers import ShippingMethodSerializer, PaymentMethodSerializer, OrderSerializer, OrderItemSerializer, OrderShippingSerializer, \
    OrderAddressHomeSerializer


class ShippingMethodViewSet(ModelViewSet):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return super().get_permissions()
    

class PaymentMethodViewSet(ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return super().get_permissions()
    

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(customer=self.request.user)
    
    def get_permissions(self):
        if self.action in ('patch', 'put'):
            return [IsAdminUser()]
        return super().get_permissions()
    

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(order__customer=self.request.user)
    
    def get_permissions(self):
        if self.action in ('patch', 'put'):
            return [IsAdminUser()]
        return super().get_permissions()
    

class OrderShippingViewSet(ModelViewSet):
    queryset = OrderShipping.objects.all()
    serializer_class = OrderShippingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(order__customer=self.request.user)
    
    def get_permissions(self):
        if self.action in ('patch', 'put'):
            return [IsAdminUser()]
        return super().get_permissions()


class OrderAddressHomeViewSet(ModelViewSet):
    queryset = OrderAddressHome.objects.all()
    serializer_class = OrderAddressHomeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(order__customer=self.request.user)
    
    def get_permissions(self):
        if self.action in ('patch', 'put'):
            return [IsAdminUser()]
        return super().get_permissions()