import pytest
from rest_framework.test import APIClient

from .factories import UserFactory


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
    client = APIClient()
    client.force_authenticate(user=customer)
    res = client.get('/api/users/me/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_user_retrieve_me_fail(client):
    # not authenticated
    res = client.get('/api/users/me/')
    assert res.status_code == 401
    
@pytest.mark.django_db
def test_user_update_me_success(customer_client):
    data = {
        'username': 'test',
        'password': 'test',
    }
    res = customer_client.put('/api/users/me/', data)
    assert res.status_code == 200
    assert res.data.get('username') == 'test'
    
@pytest.mark.django_db
def test_user_update_me_fail(customer_client):
    # missing field
    data = {
        'username': 'test'
    }
    res = customer_client.put('/api/users/me/', data)
    assert res.status_code == 400

@pytest.mark.django_db
def test_user_delete_me_success(customer_client):
    res = customer_client.delete('/api/users/me/')
    assert res.status_code == 204
    
@pytest.mark.django_db
def test_user_delete_me_fail(client):
    # not authenticated
    res = client.delete('/api/users/me/')
    assert res.status_code == 401
    
@pytest.mark.django_db
def test_customer_address_home_list(customer_client):
    res = customer_client.get('/api/customers-address-home/')
    assert res.status_code == 200
    
@pytest.mark.django_db
def test_customer_address_home_retrieve_success(client, customer_address_home):
    client.force_authenticate(user=customer_address_home.customer)
    res = client.get(f'/api/customers-address-home/{customer_address_home.pk}/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_customer_address_home_retrieve_fail(client, customer_address_home):
    # no permission
    user = UserFactory(groups='Customer')
    client.force_authenticate(user=user)
    res = client.get(f'/api/customers-address-home/{customer_address_home.pk}/')
    assert res.status_code == 404

@pytest.mark.django_db
def test_customer_address_home_create_success(customer_client, customer):
    data = {
        'customer_id': customer.pk,
        'recipient_name': 'test',
        'phone': 'test',
        'address': 'test',
        'zip_code': 'test'
    }
    res = customer_client.post('/api/customers-address-home/', data)
    assert res.status_code == 201

@pytest.mark.django_db
def test_customer_address_home_create_fail(customer_client):
    user = UserFactory(groups='Customer')
    data = {
        'customer_id': user.pk,
        'recipient_name': 'test',
        'phone': 'test',
        'address': 'test',
        'zip_code': 'test'
    }
    res = customer_client.post('/api/customers-address-home/', data)
    assert res.status_code == 400

@pytest.mark.django_db
def test_customer_address_home_update_success(customer_client, customer_address_home):
    data = {
        'customer_id': customer_address_home.customer.pk,
        'recipient_name': 'test',
        'phone': 'test',
        'address': 'test',
        'zip_code': 'test'
    }
    res = customer_client.put(f'/api/customers-address-home/{customer_address_home.pk}/', data)
    assert res.status_code == 200
    
@pytest.mark.django_db
def test_customer_address_home_update_fail(client, customer_address_home):
    # no permission
    user = UserFactory(groups='Customer')
    client.force_authenticate(user=user)
    data = {
        'recipient_name': 'test',
        'phone': 'test',
        'address': 'test',
        'zip_code': 'test'
    }
    res = client.put(f'/api/customers-address-home/{customer_address_home.pk}/', data)
    assert res.status_code == 404

@pytest.mark.django_db
def test_customer_address_home_update_fail_2(customer_client, customer_address_home):
    # no permission
    user = UserFactory(groups='Customer')
    data = {
        'customer_id': user.pk,
        'recipient_name': 'test',
        'phone': 'test',
        'address': 'test',
        'zip_code': 'test'
    }
    res = customer_client.put(f'/api/customers-address-home/{customer_address_home.pk}/', data)
    assert res.status_code == 400
    
@pytest.mark.django_db
def test_customer_address_home_delete_success(customer_client, customer_address_home):
    res = customer_client.delete(f'/api/customers-address-home/{customer_address_home.pk}/')
    assert res.status_code == 204
    
@pytest.mark.django_db
def test_customer_address_home_delete_fail(client, customer_address_home):
    # no permission
    user = UserFactory(groups='Customer')
    client.force_authenticate(user=user)
    res = client.delete(f'/api/customers-address-home/{customer_address_home.pk}/')
    assert res.status_code == 404