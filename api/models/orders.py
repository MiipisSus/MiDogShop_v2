from django.db import models


class PaymentMethods(models.Model):
  name = models.CharField(max_length=100)
  display_name = models.CharField(max_length=100)
  
  class Meta:
    db_table = 'payment_method'


PENDING, PAID, SHIPPED, ARRIVED, COMPLETED, CANCELED = 'PENDING', 'PAID', 'SHIPPED', 'ARRIVED', 'COMPLETED', 'CANCELED'
order_status = (
  (PENDING, 'pending'),
  (PAID, 'paid'),
  (SHIPPED, 'shipped'),
  (ARRIVED, 'arrived'),
  (COMPLETED, 'completed'),
  (CANCELED, 'canceled')
)

class Orders(models.Model):
  customer = models.ForeignKey('api.Customers', on_delete=models.CASCADE)
  order_number = models.CharField(max_length=100, unique=True)
  total_price = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(max_length=50, choices=order_status, default=order_status[0])
  payment_method = models.ForeignKey(PaymentMethods, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'orders'
    

class OrderItems(models.Model):
  order = models.ForeignKey(Orders, on_delete=models.CASCADE)
  product_variant = models.ForeignKey('api.ProductVariants', on_delete=models.CASCADE)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  sub_total = models.DecimalField(max_digits=10, decimal_places=2)
  
  class Meta:
    db_table = 'order_items'
    

class ShippingMethods(models.Model):
  name = models.CharField(max_length=100)
  display_name = models.CharField(max_length=100)
  
  
class OrderAddressHome(models.Model):
  recipient_name = models.CharField(max_length=100, null=False)
  phone = models.CharField(max_length=100)
  address = models.TextField()
  zip_code = models.CharField(max_length=6)
  

class OrderShippings(models.Model):
  order = models.ForeignKey(Orders, on_delete=models.CASCADE)
  tracking_number = models.CharField(max_length=100)
  customer_message = models.TextField()
  
  shipping_method = models.ForeignKey(ShippingMethods, on_delete=models.SET_NULL, null=True)
  address_home = models.ForeignKey(OrderAddressHome, on_delete=models.SET_NULL, null=True)
  
