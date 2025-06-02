from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    class UsageType(models.TextChoices):
        DOG = 'DOG', _('狗')
        CAT = 'CAT', _('貓')
        GENERAL = 'GENERAL', _('通用')
        
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    usage_type = models.CharField(
        max_length=50, choices=UsageType.choices, default=UsageType.DOG)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_usage_type(self):
        return self.UsageType(self.usage_type)
        
    class Meta:
        db_table = 'products'


class ProductOption(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product_options'


class ProductValue(models.Model):
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    class Meta:
        db_table = 'product_values'
        
        
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    values = models.ManyToManyField('ProductValue', related_name='variants')

    class Meta:
        db_table = 'product_variants'