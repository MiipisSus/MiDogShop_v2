import pytest

from .factories import *
from api.models.products import Product, Category, ProductOption


@pytest.mark.django_db
def test_category_list(client):
    res = client.get('/api/categories/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_category_retrieve_success(client):
    category = Category.objects.order_by('?').first()
    res = client.get(f'/api/categories/{category.pk}/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_category_retrieve_fail(client):
    res = client.get(f'/api/categories/100/')
    assert res.status_code == 404
    
@pytest.mark.django_db
def test_category_create_success(manager_client):
    data = {
        'name': 'test',
        'display_name': 'test',
    }
    res = manager_client.post('/api/categories/', data)
    assert res.status_code == 201

@pytest.mark.django_db
def test_category_create_fail(manager_client):
    # missing field
    data = {
        'name': 'test',
    }
    res = manager_client.post('/api/categories/', data)
    assert res.status_code == 400
    
    # unauthorized
    manager_client.logout()
    res = manager_client.post('/api/categories/', data)
    assert res.status_code == 401
    
@pytest.mark.django_db
def test_category_update_success(manager_client, category):
    data = {
        'name': 'test',
        'display_name': 'test',
    }
    res = manager_client.put(f'/api/categories/{category.pk}/', data)
    assert res.status_code == 200

@pytest.mark.django_db
def test_category_update_fail(staff_client, category):
    # no permission
    data = {
        'name': 'test',
    }
    res = staff_client.put(f'/api/categories/{category.pk}/', data)
    assert res.status_code == 403
    
@pytest.mark.django_db
def test_category_delete_success(manager_client, category):
    res = manager_client.delete(f'/api/categories/{category.pk}/')
    assert res.status_code == 204

@pytest.mark.django_db
def test_category_delete_fail(staff_client, category):
    # no permission
    res = staff_client.delete(f'/api/categories/{category.pk}/')
    assert res.status_code == 403
    
@pytest.mark.django_db
def test_product_list(customer_client):
    ProductFactory.create_batch(5)
    res = customer_client.get('/api/products/')
    assert res.status_code == 200
    
@pytest.mark.django_db
def test_product_retrieve(customer_client, product):
    res = customer_client.get(f'/api/products/{product.pk}/')
    assert res.status_code == 200

@pytest.mark.django_db
def test_product_retrieve_fail(customer_client):
    res = customer_client.get(f'/api/products/100/')
    assert res.status_code == 404
    
@pytest.mark.django_db
def test_product_create_success(manager_client):
    data = {
        'name': 'test',
        'description': 'test',
        'base_price': 10.0,
        'usage_type': Product.UsageType.DOG,
    }
    res = manager_client.post('/api/products/', data)
    assert res.status_code == 201

@pytest.mark.django_db
def test_product_create_fail(manager_client):
    # missing field
    data = {
        'name': 'test',
    }
    res = manager_client.post('/api/products/', data)
    assert res.status_code == 400
    
    # unauthorized
    manager_client.logout()
    res = manager_client.post('/api/products/', data)
    assert res.status_code == 401
    
@pytest.mark.django_db
def test_product_update_success(manager_client, product):
    data = {
        'name': 'test',
        'description': 'test',
        'base_price': 10.0,
        'usage_type': Product.UsageType.DOG,
    }
    res = manager_client.put(f'/api/products/{product.pk}/', data)
    assert res.status_code == 200
    assert res.data.get('name') == 'test'
    
@pytest.mark.django_db
def test_product_update_fail(staff_client, product):
    # no permission
    data = {
        'name': 'test',
    }
    res = staff_client.patch(f'/api/products/{product.pk}/', data)
    assert res.status_code == 403
    
@pytest.mark.django_db
def test_product_delete_success(manager_client, product):
    res = manager_client.delete(f'/api/products/{product.pk}/')
    assert res.status_code == 204

@pytest.mark.django_db
def test_product_delete_fail(staff_client, product):
    # no permission
    res = staff_client.delete(f'/api/products/{product.pk}/')
    assert res.status_code == 403

@pytest.mark.django_db
def test_product_variant_retrieve(customer_client, product):
    res = customer_client.get(f'/api/product-variants/{product.variants.first().pk}/')
    assert res.status_code == 200
    
@pytest.mark.django_db
def test_product_variant_create_success(manager_client, product, product_value):
    data = {
        'product': product.pk,
        'sku': 'test',
        'price': 10.0,
        'stock': 10,
        'value_ids': [product_value.pk],
    }
    res = manager_client.post('/api/product-variants/', data)
    assert res.status_code == 201

@pytest.mark.django_db
def test_product_variant_create_fail(staff_client, product, product_value):
    # no permission
    data = {
        'product': product.pk,
        'sku': 'test',
        'price': 10.0,
        'stock': 10,
        'value_ids': [product_value.pk],
    }
    res = staff_client.post('/api/product-variants/', data)
    assert res.status_code == 403
    
@pytest.mark.django_db
def test_product_variant_update_success(manager_client, product_variant):
    data = {
        'sku': 'test',
        'price': 10.0,
        'stock': 10
    }
    res = manager_client.patch(f'/api/product-variants/{product_variant.pk}/', data)
    assert res.status_code == 200
    assert res.data.get('sku') == 'test'

@pytest.mark.django_db
def test_product_variant_update_fail(staff_client, product_variant):
    # no permission
    data = {
        'sku': 'test',
        'price': 10.0,
        'stock': 10
    }
    res = staff_client.patch(f'/api/product-variants/{product_variant.pk}/', data)
    assert res.status_code == 403
    
@pytest.mark.django_db
def test_product_variant_delete_success(manager_client, product_variant):
    res = manager_client.delete(f'/api/product-variants/{product_variant.pk}/')
    assert res.status_code == 204
    
@pytest.mark.django_db
def test_product_variant_delete_fail(staff_client, product_variant):
    # no permission
    res = staff_client.delete(f'/api/product-variants/{product_variant.pk}/')
    assert res.status_code == 403
    
@pytest.mark.django_db
def test_product_value_create_success(manager_client):
    data = {
        'option_id': ProductOption.objects.first().pk,
        'value': 'test',
    }
    res = manager_client.post('/api/product-values/', data)
    assert res.status_code == 201
    
@pytest.mark.django_db
def test_product_value_create_fail(staff_client):
    # no permission
    data = {
        'option_id': ProductOption.objects.first().pk,
        'value': 'test',
    }
    res = staff_client.post('/api/product-values/', data)
    assert res.status_code == 403

@pytest.mark.django_db
def test_product_value_update_success(manager_client, product_value):
    data = {
        'value': 'test',
    }
    res = manager_client.patch(f'/api/product-values/{product_value.pk}/', data)
    assert res.status_code == 200
    assert res.data.get('value') == 'test'

@pytest.mark.django_db
def test_product_value_update_fail(staff_client, product_value):
    # no permission
    data = {
        'value': 'test',
    }
    res = staff_client.patch(f'/api/product-values/{product_value.pk}/', data)
    assert res.status_code == 403

@pytest.mark.django_db
def test_product_value_delete_success(manager_client, product_value):
    res = manager_client.delete(f'/api/product-values/{product_value.pk}/')
    assert res.status_code == 204
    
@pytest.mark.django_db
def test_product_value_delete_fail(staff_client, product_value):
    # no permission
    res = staff_client.delete(f'/api/product-values/{product_value.pk}/')
    assert res.status_code == 403