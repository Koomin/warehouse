from rest_framework import serializers
from products.models import Product, Unit, ProductCategory


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'short_name', ]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['name', 'product_code', ]


class ProductSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.short_name')
    category_name = serializers.CharField(source='category.name', allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'pkwiu', 'optima_id', 'category', 'unit', 'unit_name', 'value',
                  'retail_value', 'category_name', ]
