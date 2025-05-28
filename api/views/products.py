from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import SAFE_METHODS

from api.models import Product, Category, ProductVariant, ProductValue, ProductOption
from api.serializers.products import ProductSerializer, CategorySerializer, ProductVariantSerializer, ProductValueSerializer, ProductOptionSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
    

class ProductVariantViewSet(ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
    

class ProductValueViewSet(ModelViewSet):
    queryset = ProductValue.objects.all()
    serializer_class = ProductValueSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
    
class ProductOptionViewSet(ModelViewSet):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()