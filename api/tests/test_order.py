import pytest

from api.models.orders import Order
from .factories import UserFactory

@pytest.mark.django_db
def test_order_list(customer_client):
    res = customer_client.get('/api/orders/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_order_retrieve(client, order):
    client.force_authenticate(user=order.customer)
    res = client.get(f'/api/orders/{order.pk}/')
    assert res.status_code == 200
    
@pytest.mark.django_db
def test_order_create(client, customer):
    client.force_authenticate(user=customer)
    data = {
        'customer_id': customer.pk,
        'order_number': 'test',
        'total_price': 10.0,
        'status': Order.OrderStatus.PENDING,
        'payment_method': 1
    }
    res = client.post('/api/orders/', data)
    assert res.status_code == 201
    
@pytest.mark.django_db
def test_order_create_fail(customer_client):
    customer = UserFactory(groups='Customer')
    data = {
        'customer_id': customer.pk,
        'order_number': 'test',
        'total_price': 10.0,
        'status': Order.OrderStatus.PENDING,
        'payment_method': 1
    }
    res = customer_client.post('/api/orders/', data)
    assert res.status_code == 400

@pytest.mark.django_db
def test_order_update_success(staff_client, order):
    data = {
        'order_number': 'test'
    }
    res = staff_client.patch(f'/api/orders/{order.pk}/', data)
    assert res.status_code == 200

@pytest.mark.django_db
def test_order_update_fail(client, order):
    # no permission
    data = {
        'order_number': 'test'
    }
    client.force_authenticate(user=order.customer)
    res = client.patch(f'/api/orders/{order.pk}/', data)
    assert res.status_code == 403

@pytest.mark.django_db
def test_order_delete_success(staff_client, order):
    res = staff_client.delete(f'/api/orders/{order.pk}/')
    assert res.status_code == 204
    
@pytest.mark.django_db
def test_order_delete_fail(client, order):
    # no permission
    client.force_authenticate(user=order.customer)
    res = client.delete(f'/api/orders/{order.pk}/')
    assert res.status_code == 403

@pytest.mark.django_db
def test_order_item_retrieve(client, order_item):
    client.force_authenticate(user=order_item.order.customer)
    res = client.get(f'/api/order-items/{order_item.pk}/')
    assert res.status_code == 200
    
@pytest.mark.django_db
def test_order_item_create(client, order, product_variant):
    client.force_authenticate(user=order.customer)
    data = {
        'order_id': order.id,
        'variant_id': product_variant.id,
        'quantity': 1,
        'price': 10.0,
        'sub_total': 10.0
    }
    res = client.post('/api/order-items/', data)
    assert res.status_code == 201
    #FIXME: The customer should not be able to create order item owned by another customer