from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_variants'


class ProductOption(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_options'


class ProductValue(models.Model):
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_values'


class VariantValueMap(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    value_id = models.ForeignKey(ProductValue, on_delete=models.CASCADE)

    class Meta:
        db_table = 'variant_value_map'

