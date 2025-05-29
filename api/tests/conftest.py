import pytest
from django.contrib.auth.models import Group
from rest_framework.test import APIClient

from .factories import *
from .common import *


@pytest.fixture(autouse=True, scope='session')
def create_default_groups(django_db_setup, django_db_blocker):
    #FIXME
    with django_db_blocker.unblock():
        customer = GroupFactory(id=1, name='Customer')
        staff = GroupFactory(id=2, name='Staff')
        manager = GroupFactory(id=3, name='Manager')
        
@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def customer():
    return UserFactory(is_superuser=False, is_staff=False, groups=[1])

@pytest.fixture
def admin():
    return UserFactory(is_superuser=True, is_staff=True)

@pytest.fixture
def customer_client(client, customer):
    client.force_authenticate(user=customer)
    return client

@pytest.fixture
def admin_client(client, admin):
    client.force_authenticate(user=admin)
    return client