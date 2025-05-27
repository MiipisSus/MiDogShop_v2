from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from api.models import Product, Category, ProductVariant, ProductOption
from api.serializers.products import ProductSerializer, CategorySerializer, ProductVariantSerializer, ProductOptionSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return []
        return super().get_permissions()

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return []
        return super().get_permissions()
    

class ProductVariantViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return []
        return super().get_permissions()
    
class ProductOptionViewSet(ModelViewSet):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return []
        return super().get_permissions()