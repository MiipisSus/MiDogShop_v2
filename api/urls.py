from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CustomerAddressHomeViewSet, CategoryViewSet, ProductViewSet, ProductVariantViewSet, ProductOptionViewSet, \
    ProductValueViewSet, ShippingMethodViewSet, PaymentMethodViewSet, OrderViewSet, \
    OrderItemViewSet, OrderShippingViewSet, OrderAddressHomeViewSet, CustomTokenObtainPairView, CustomTokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('customers-address-home', CustomerAddressHomeViewSet, basename='customer-address-home')

router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('product-variants', ProductVariantViewSet)
router.register('product-values', ProductValueViewSet)
router.register('product-options', ProductOptionViewSet)

router.register('shipping-methods', ShippingMethodViewSet)
router.register('payment-methods', PaymentMethodViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('order-shipping', OrderShippingViewSet)
router.register('order-address-home', OrderAddressHomeViewSet)
urlpatterns = router.urls + \
    [
        path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    ]
