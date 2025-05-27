from django.db import models
from django.contrib.auth.models import AbstractUser


CUSTOMER, ADMIN = 'customer', 'admin'
user_type = [(CUSTOMER, 'Customer'), (ADMIN, 'Admin')]


class User(AbstractUser):
    phone = models.CharField(max_length=100, null=True)

    def is_customer(self):
        return self.groups.filter(name='Customer').exists()

    class Meta:
        db_table = 'users'


class CustomerAddressHome(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    zip_code = models.CharField(max_length=6)

    class Meta:
        db_table = 'customer_address_home'
