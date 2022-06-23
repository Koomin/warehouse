from django.contrib import admin
from .models import ProductCategory, Product, Unit
from warehouse_app.warehouse.admin import WarehouseAdmin


@admin.register(ProductCategory)
class ProductCategoryAdmin(WarehouseAdmin):
    list_display = ('product_code', 'name',)
    search_fields = ['name', 'product_code', ]


@admin.register(Product)
class ProductAdmin(WarehouseAdmin):
    list_display = ('code', 'name', 'category', 'unit', 'optima_id',)
    search_fields = ['name', 'code', ]
    list_filter = ['category__name', 'unit__short_name']


@admin.register(Unit)
class UnitAdmin(WarehouseAdmin):
    list_display = ('short_name',)
    search_fields = ['short_name']
