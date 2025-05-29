from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import SAFE_METHODS
from drf_spectacular.utils import extend_schema, extend_schema_view

from api.models import Product, Category, ProductVariant, ProductValue, ProductOption
from api.serializers.products import ProductSerializer, CategorySerializer, ProductVariantSerializer, ProductValueSerializer, ProductOptionSerializer
from api.common import PERMMISIONS_DOCS


@extend_schema_view(
    list=extend_schema(summary=f"取得所有商品類別 {PERMMISIONS_DOCS.NoAuth}"),
    retrieve=extend_schema(summary=f"取得單一商品類別 {PERMMISIONS_DOCS.NoAuth}"),
    create=extend_schema(summary=f"新增商品類別 {PERMMISIONS_DOCS.IsAdminUser}"),
    update=extend_schema(summary=f"更新商品類別 {PERMMISIONS_DOCS.IsAdminUser}"),
    partial_update=extend_schema(summary=f"更新商品類別 {PERMMISIONS_DOCS.IsAdminUser}"),
    destroy=extend_schema(summary=f"刪除商品類別 {PERMMISIONS_DOCS.IsAdminUser}"),
)
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


@extend_schema_view(
    list=extend_schema(summary=f"取得所有商品 {PERMMISIONS_DOCS.NoAuth}"),
    retrieve=extend_schema(summary=f"取得單一商品 {PERMMISIONS_DOCS.NoAuth}"),
    create=extend_schema(summary=f"新增商品 {PERMMISIONS_DOCS.IsAdminUser}"),
    update=extend_schema(summary=f"更新商品 {PERMMISIONS_DOCS.IsAdminUser}"),
    partial_update=extend_schema(summary=f"更新商品 {PERMMISIONS_DOCS.IsAdminUser}"),
    destroy=extend_schema(summary=f"刪除商品 {PERMMISIONS_DOCS.IsAdminUser}"),
)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
    

@extend_schema_view(
    list=extend_schema(summary=f"取得所有商品規格 {PERMMISIONS_DOCS.NoAuth}"),
    retrieve=extend_schema(summary=f"取得單一商品規格 {PERMMISIONS_DOCS.NoAuth}"),
    create=extend_schema(summary=f"新增商品規格 {PERMMISIONS_DOCS.IsAdminUser}"),
    update=extend_schema(summary=f"更新商品規格 {PERMMISIONS_DOCS.IsAdminUser}"),
    partial_update=extend_schema(summary=f"更新商品規格 {PERMMISIONS_DOCS.IsAdminUser}"),
    destroy=extend_schema(summary=f"刪除商品規格 {PERMMISIONS_DOCS.IsAdminUser}"),
)
class ProductVariantViewSet(ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
    

@extend_schema_view(
    list=extend_schema(summary=f"取得所有商品規格值（例：紅色） {PERMMISIONS_DOCS.NoAuth}"),
    retrieve=extend_schema(summary=f"取得單一商品規格值 {PERMMISIONS_DOCS.NoAuth}"),
    create=extend_schema(summary=f"新增商品規格值 {PERMMISIONS_DOCS.IsAdminUser}"),
    update=extend_schema(summary=f"更新商品規格值 {PERMMISIONS_DOCS.IsAdminUser}"),
    partial_update=extend_schema(summary=f"更新商品規格值 {PERMMISIONS_DOCS.IsAdminUser}"),
    destroy=extend_schema(summary=f"刪除商品規格值 {PERMMISIONS_DOCS.IsAdminUser}"),
)
class ProductValueViewSet(ModelViewSet):
    queryset = ProductValue.objects.all()
    serializer_class = ProductValueSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
    

@extend_schema_view(
    list=extend_schema(summary=f"取得所有商品選項（例：顏色、尺寸）{PERMMISIONS_DOCS.NoAuth}"),
    retrieve=extend_schema(summary=f"取得單一商品選項 {PERMMISIONS_DOCS.NoAuth}"),
    create=extend_schema(summary=f"新增商品選項 {PERMMISIONS_DOCS.IsAdminUser}"),
    update=extend_schema(summary=f"更新商品選項 {PERMMISIONS_DOCS.IsAdminUser}"),
    partial_update=extend_schema(summary=f"更新商品選項 {PERMMISIONS_DOCS.IsAdminUser}"),
    destroy=extend_schema(summary=f"刪除商品選項 {PERMMISIONS_DOCS.IsAdminUser}"),
)
class ProductOptionViewSet(ModelViewSet):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()