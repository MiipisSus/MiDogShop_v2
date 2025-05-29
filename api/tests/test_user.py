import pytest

from .factories import UserFactory
from .common import DEFAULT_PASSWORD


@pytest.mark.django_db
def test_user_list_success(customer_client):
    res = customer_client.get('/api/users/')
    assert res.status_code == 200
    
@pytest.mark.django_db
def test_user_list_fail(client):
    res = client.get('/api/users/')
    assert res.status_code == 401

@pytest.mark.django_db
def test_user_retrieve_success(admin_client, customer):
    res = admin_client.get(f'/api/users/{customer.pk}/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_user_retrieve_fail(customer_client):
    # user does not exist
    res = customer_client.get(f'/api/users/3/')
    assert res.status_code == 404
    
@pytest.mark.django_db
def test_user_create_success(client):
    data = {
        'username': 'test',
        'password': 'test',
    }
    res = client.post('/api/users/', data)
    assert res.status_code == 201
    
@pytest.mark.django_db
def test_user_create_fail(client, customer):
    # missing field
    data = {
        'username': 'test'
    }
    res = client.post('/api/users/', data)
    assert res.status_code == 400
    # duplicate username
    data = {
        'username': customer.username,
        'password': 'test',
    }
    res = client.post('/api/users/', data)
    assert res.status_code == 400

@pytest.mark.django_db
def test_user_update_success(admin_client, customer):
    
    data = {
        'username': 'test',
        'password': 'test',
    }
    res = admin_client.put(f'/api/users/{customer.pk}/', data)
    assert res.status_code == 200
    assert res.data.get('username') == 'test'

@pytest.mark.django_db
def test_user_update_fail(admin_client):
    # user does not exist
    data = {
        'username': 'test',
        'password': 'test',
    }
    res = admin_client.put(f'/api/users/100/', data)
    assert res.status_code == 404
    
    # duplicate username
    user1, user2 = UserFactory.create_batch(2)
    data = {
        'username': user1.username,
        'password': 'test',
    }
    res = admin_client.put(f'/api/users/{user2.pk}/', data)
    assert res.status_code == 400
    
@pytest.mark.django_db
def test_user_delete_success(admin_client, customer):
    res = admin_client.delete(f'/api/users/{customer.pk}/')
    assert res.status_code == 204

@pytest.mark.django_db
def test_user_delete_fail(admin_client):
    # user does not exist
    res = admin_client.delete(f'/api/users/100/')
    assert res.status_code == 404

@pytest.mark.django_db
def test_user_retrieve_me_success(customer):
    from rest_framework.test import APIClient
    from api.models import User
    client = APIClient()
    client.force_authenticate(user=customer)
    print(f"Customer: {customer}")
    print(f"Customer ID: {customer.id}")
    print(f"User exists: {User.objects.filter(id=customer.id).exists()}")
    res = client.get('/api/users/me/')
    print(res.data)
    assert res.status_code == 200

@pytest.mark.django_db
def test_user_retrieve_me_fail(client):
    res = client.get('/api/users/me/')
    assert res.status_code == 401
    
@pytest.mark.django_db
def test_user_update_me_success(customer_client):
    # FIXME: 404
    data = {
        'username': 'test',
        'password': 'test',
    }
    res = customer_client.put('/api/users/me/', data)
    assert res.status_code == 200
    assert res.data.get('username') == 'test'
