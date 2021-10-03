from django.contrib import admin
from .models import ProductCategory, Product, Unit
from warehouse.admin import WarehouseAdmin


class ProductCategoryAdmin(WarehouseAdmin):
    list_display = ('product_code', 'name',)
    search_fields = ['name', 'product_code', ]


class ProductAdmin(WarehouseAdmin):
    list_display = ('code', 'name', 'category', 'unit', 'optima_id',)
    search_fields = ['name', 'code', ]
    list_filter = ['category__name', 'unit__short_name']


class UnitAdmin(WarehouseAdmin):
    list_display = ('short_name', 'name')
    search_fields = ['short_name', 'name']


admin.site.register(Unit, UnitAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
