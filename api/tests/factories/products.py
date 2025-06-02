import factory
from factory.django import DjangoModelFactory
from factory import fuzzy

from api.models.products import Product, ProductVariant, ProductValue, ProductOption, Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    display_name = factory.Faker('word')
    
    
class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    base_price = fuzzy.FuzzyDecimal(10.0, 100.0)
    usage_type = fuzzy.FuzzyChoice(Product.UsageType.choices)

    @factory.lazy_attribute
    def category(self):
        return Category.objects.order_by('?').first()
    
    @factory.post_generation
    def variants(self, create, extracted, **kwargs):
        if extracted:
            for variant in extracted:
                variant.product = self
                variant.save()
        else:
            for _ in range(2):
                ProductVariantFactory(product=self)
                

class ProductValueFactory(DjangoModelFactory):
    class Meta:
        model = ProductValue

    @factory.lazy_attribute
    def option(self):
        return ProductOption.objects.order_by('?').first()

    value = factory.Faker('word')


class ProductVariantFactory(DjangoModelFactory):
    class Meta:
        model = ProductVariant

    product = factory.SubFactory(ProductFactory)
    sku = factory.Sequence(lambda n: f'SKU{n:05d}')
    price = fuzzy.FuzzyDecimal(10.0, 200.0)
    stock = fuzzy.FuzzyInteger(0, 100)

    @factory.post_generation
    def values(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for value in extracted:
                self.values.add(value)
        else:
            # 預設給 variant 加上兩個 value (顏色與尺寸)
            options = ProductOption.objects.all()
            for option in options:
                val = ProductValueFactory(option=option)
                self.values.add(val)