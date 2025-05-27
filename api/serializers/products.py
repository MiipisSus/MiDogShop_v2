from rest_framework import serializers

from api.models import Category, Product, ProductVariant, ProductOption, ProductValue


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        read_only_fields = ['created_at', 'updated_at']
        

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'
        

class ProductValueSerializer(serializers.ModelSerializer):
    option = ProductOptionSerializer()
    class Meta:
        model = ProductValue
        fields = '__all__'
        
        
class ProductVariantSerializer(serializers.ModelSerializer):
    value_id = serializers.IntegerField(source='value', write_only=True)
    value = ProductValueSerializer(read_only=True)
    class Meta:
        model = ProductVariant
        fields = '__all__'
        
        read_only_fields = ['created_at', 'updated_at']
        
    def create(self, validated_data):
        return super().create(validated_data)
    
    # FIXME: 1. The value_id and value doesn't show properly on the docs
    #        2. The create/update method should input option/value to create ProductValue as well
    #        3. The list method shows 404 NOT FOUND, not 200 OK
