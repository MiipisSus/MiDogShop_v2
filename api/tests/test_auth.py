import pytest
from rest_framework.test import APIClient

from .common import DEFAULT_PASSWORD


@pytest.mark.django_db
def test_user_login_success(client, customer):
    client = APIClient()
    res = client.post('/api/login/', 
                      {'username': customer.username,
                       'password': DEFAULT_PASSWORD})
    assert res.status_code == 200
    assert 'access' in res.data
    
@pytest.mark.django_db
def test_user_login_fail(client, customer):
    client = APIClient()
    res = client.post('/api/login/', 
                      {'username': customer.username,
                       'password': "wrong"})
    assert res.status_code == 401