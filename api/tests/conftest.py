import pytest
from django.contrib.auth.models import Group
from rest_framework.test import APIClient

from .factories import *
from .common import *

        
@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def customer():
    return UserFactory(is_superuser=False, is_staff=False, groups='Customer')

@pytest.fixture
def admin():
    return UserFactory(is_superuser=True, is_staff=True)

@pytest.fixture
def staff():
    return UserFactory(is_superuser=False, is_staff=True, groups='Staff')

@pytest.fixture
def manager():
    return UserFactory(is_superuser=False, is_staff=True, groups='Manager')

@pytest.fixture
def customer_client(client, customer):
    client.force_authenticate(user=customer)
    return client

@pytest.fixture
def admin_client(client, admin):
    client.force_authenticate(user=admin)
    return client

@pytest.fixture
def staff_client(client, staff):
    client.force_authenticate(user=staff)
    return client

@pytest.fixture
def manager_client(client, manager):
    client.force_authenticate(user=manager)
    return client

@pytest.fixture
def product():
    return ProductFactory()

@pytest.fixture
def product_variant(product):
    return ProductVariantFactory(product=product)

@pytest.fixture
def product_value():
    return ProductValueFactory()

@pytest.fixture
def category():
    return CategoryFactory()

@pytest.fixture
def order(customer):
    return OrderFactory(customer=customer)

@pytest.fixture
def order_item(order):
    return OrderItemFactory(order=order)