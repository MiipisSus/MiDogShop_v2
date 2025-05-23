from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'categories'


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'


class ProductVariants(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_variants'


class ProductOptions(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_options'


class ProductValues(models.Model):
    option = models.ForeignKey(ProductOptions, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_values'


class VariantValueMap(models.Model):
    variant = models.ForeignKey(ProductVariants, on_delete=models.CASCADE)
    value_id = models.ForeignKey(ProductValues, on_delete=models.CASCADE)

    class Meta:
        db_table = 'variant_value_map'

