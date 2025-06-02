import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from api.models.orders import Order, OrderItem, PaymentMethod, OrderShipping, ShippingMethod, \
    OrderAddressHome


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
        
    customer = factory.SubFactory('api.tests.factories.users.UserFactory')
    order_number = factory.Sequence(lambda n: f'ORDER{n:05d}')
    total_price = fuzzy.FuzzyDecimal(10.0, 1000.0)
    status = fuzzy.FuzzyChoice(Order.OrderStatus.choices)

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for item in extracted:
                item.order = self
                item.save()
        else:
            for _ in range(2):
                OrderItemFactory(order=self)
    
    @factory.post_generation
    def shippings(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            self.shipping = extracted
        else:
            OrderShippingFactory(order=self)
                
    @factory.lazy_attribute
    def payment_method(self):
        return PaymentMethod.objects.order_by('?').first()
                

class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem
        
    order = factory.SubFactory(OrderFactory)
    product_variant = factory.SubFactory('api.tests.factories.products.ProductVariantFactory')
    quantity = fuzzy.FuzzyInteger(1, 10)
    price = fuzzy.FuzzyDecimal(10.0, 1000.0)
    sub_total = fuzzy.FuzzyDecimal(10.0, 1000.0)


class OrderShippingFactory(DjangoModelFactory):
    class Meta:
        model = OrderShipping
        
    order = factory.SubFactory(OrderFactory)
    tracking_number = factory.Sequence(lambda n: f'TRACKING{n:05d}')
    customer_message = factory.Faker('sentence')
    
    @factory.lazy_attribute
    def shipping_method(self):
        return ShippingMethod.objects.order_by('?').first()
    
    @factory.post_generation
    def address_home(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            self.address_home = extracted
        else:
            self.address_home = OrderAddressHomeFactory()
            
class OrderAddressHomeFactory(DjangoModelFactory):
    class Meta:
        model = OrderAddressHome
        
    recipient_name = factory.Faker('name')
    phone = factory.Faker('phone_number')
    address = factory.Faker('address')
    zip_code = factory.Faker('postcode')
    