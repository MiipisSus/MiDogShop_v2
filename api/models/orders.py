from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'payment_methods'


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING', _('待付款')
        PAID = 'PAID', _('已付款')
        SHIPPED = 'SHIPPED', _('已出貨')
        ARRIVED = 'ARRIVED', _('已到貨')
        COMPLETED = 'COMPLETED', _('已完成')
        CANCELED = 'CANCELED', _('已取消')
        
    customer = models.ForeignKey('api.User', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=100, unique=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_status(self):
        return self.OrderStatus(self.status)

    class Meta:
        db_table = 'orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_variant = models.ForeignKey(
        'api.ProductVariant', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'


class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'shipping_methods'


class OrderAddressHome(models.Model):
    recipient_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    zip_code = models.CharField(max_length=6)

    class Meta:
        db_table = 'order_address_home'


class OrderShipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shippings')
    tracking_number = models.CharField(max_length=100)
    customer_message = models.TextField()

    shipping_method = models.ForeignKey(
        ShippingMethod, on_delete=models.SET_NULL, null=True)
    address_home = models.ForeignKey(
        OrderAddressHome, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'order_shippings'
