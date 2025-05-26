from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CustomerAddressHomeViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('customers/address/home', CustomerAddressHomeViewSet)

urlpatterns = router.urls