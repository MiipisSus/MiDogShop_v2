from rest_framework import serializers

from api.models import Category, Product, ProductVariant, ProductOption, ProductValue


class CategorySerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='parent', required=False, write_only=True
    )
    parent = serializers.SerializerMethodField(read_only=True)
    children = serializers.SerializerMethodField()
    
    def get_parent(self, obj):
        return {'id': obj.parent.id, 'name': obj.parent.name} if obj.parent else None
        
    def get_children(self, obj):
        return [{'id': child.id, 'name': child.name} for child in obj.children.all()]
    
    class Meta:
        model = Category
        fields = '__all__'
        

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'
        

class ProductValueSerializer(serializers.ModelSerializer):
    option_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductOption.objects.all(), source='option', write_only=True
    )
    option = ProductOptionSerializer(read_only=True)
    class Meta:
        model = ProductValue
        fields = '__all__'
        
        
class ProductVariantSerializer(serializers.ModelSerializer):
    value_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ProductValue.objects.all(), source='values', write_only=True
    )
    values = ProductValueSerializer(many=True, read_only=True)
    class Meta:
        model = ProductVariant
        fields = '__all__'
        
        read_only_fields = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
        read_only_fields = ['created_at', 'updated_at']