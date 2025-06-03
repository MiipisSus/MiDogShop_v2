from rest_framework import serializers

from api.models import User, Order, OrderItem, OrderShipping, OrderAddressHome, \
    ShippingMethod, PaymentMethod, ProductVariant
from api.serializers import ProductVariantSerializer


class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = '__all__'
        

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
     
        
class OrderAddressHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAddressHome
        fields = '__all__'
        

class OrderShippingSerializer(serializers.ModelSerializer):
    shipping_method_id = serializers.PrimaryKeyRelatedField(
        queryset=ShippingMethod.objects.all(),
        source='shipping_method',
        write_only=True
    )
    address_home_id = serializers.PrimaryKeyRelatedField(
        queryset=OrderAddressHome.objects.all(),
        source='address_home',
        write_only=True
    )
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(),
        source='order',
        write_only=True
    )
    address_home = OrderAddressHomeSerializer(read_only=True)
    class Meta:
        model = OrderShipping
        exclude = ['shipping_method', 'order']
        
    def validate_order_id(self, value):
        request = self.context.get('request')
        if not request.user.is_superuser:
            if value.customer != request.user:
                raise serializers.ValidationError('You can only access to your own order.')
        return value
        

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(),
        source='order',
        write_only=True
    )
    variant_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all(),
        source='product_variant',
        write_only=True
    )
    variant = ProductVariantSerializer(source='product_variant', read_only=True)
    
    class Meta:
        model = OrderItem
        exclude = ['product_variant', 'order']
    
    def validate_order_id(self, value):
        request = self.context.get('request')
        if not request.user.is_superuser:
            if value.customer != request.user:
                raise serializers.ValidationError('You can only access to your own order.')
        return value


class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='customer'
    )
    items = OrderItemSerializer(many=True, read_only=True)
    shippings = OrderShippingSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        exclude = ['customer']
        
    def validate_customer_id(self, value):
        request = self.context.get('request')
        if not request.user.is_superuser:
            if value != request.user:
                raise serializers.ValidationError('You can only access to your own order.')
        return value