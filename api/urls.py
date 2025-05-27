from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CustomerAddressHomeViewSet, CategoryViewSet, ProductViewSet, ProductVariantViewSet, ProductOptionViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('customers/address/home', CustomerAddressHomeViewSet, basename='customer-address-home')
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('products/variants', ProductVariantViewSet, basename='product-variant')
router.register('products/options', ProductOptionViewSet, basename='product-option')

urlpatterns = router.urls
