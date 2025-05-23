from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Category, Product, ProductVariant, ProductValue, ProductOption, VariantValueMap

admin.site.register(User, UserAdmin)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductValue)
admin.site.register(ProductOption)
admin.site.register(VariantValueMap)
