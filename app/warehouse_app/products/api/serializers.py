from rest_framework import serializers
from products.models import Product, Unit, ProductCategory, ProductAvailability


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['uuid', 'short_name', ]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['uuid', 'name', 'product_code', ]


class ProductSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.short_name')
    category_name = serializers.CharField(source='category.name', allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ['uuid', 'name', 'code', 'pkwiu', 'optima_id', 'category', 'unit', 'unit_name', 'value',
                  'retail_value', 'category_name', ]


class ProductAvailabilitySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_code = serializers.CharField(source='product.code')
    store_short_name = serializers.CharField(source='store.short_name')
    store_name = serializers.CharField(source='store.name')
    unit = serializers.CharField(source='unit.short_name')

    class Meta:
        model = ProductAvailability
        fields = ['uuid', 'product', 'product_name', 'product_code', 'store_name', 'store_short_name', 'quantity',
                  'value', 'unit']
