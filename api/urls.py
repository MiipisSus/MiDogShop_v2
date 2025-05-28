from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import UserViewSet, CustomerAddressHomeViewSet, CategoryViewSet, ProductViewSet, ProductVariantViewSet, ProductOptionViewSet, \
    ProductValueViewSet, ShippingMethodViewSet, PaymentMethodViewSet, OrderViewSet, OrderItemViewSet, OrderShippingViewSet, OrderAddressHomeViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('customers-address-home', CustomerAddressHomeViewSet, basename='customer-address-home')

router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('product-variants', ProductVariantViewSet, basename='product-variant')
router.register('product-values', ProductValueViewSet, basename='product-value')
router.register('product-options', ProductOptionViewSet, basename='product-option')

router.register('shipping-methods', ShippingMethodViewSet, basename='shipping-method')
router.register('payment-methods', PaymentMethodViewSet, basename='payment-method')
router.register('order', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('order-shipping', OrderShippingViewSet)
router.register('order-address-home', OrderAddressHomeViewSet)
urlpatterns = router.urls