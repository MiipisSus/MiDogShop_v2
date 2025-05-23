from django.db import models


class Customers(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=128)
    
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField()
    
    class Meta:
        db_table = 'customers'


class CustomerAddressHome(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    zip_code = models.CharField(max_length=6)
    
    class Meta:
        db_table = 'customer_address_home'
    
    
class Admins(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField()
    
    class Meta:
        db_table = 'admins'