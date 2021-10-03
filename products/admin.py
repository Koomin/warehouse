from django.contrib import admin
from .models import ProductCategory, Product
from warehouse.admin import WarehouseAdmin


class ProductCategoryAdmin(WarehouseAdmin):
    list_display = ('product_code', 'name',)
    search_fields = ['name', 'product_code', ]


class ProductAdmin(WarehouseAdmin):
    list_display = ('code', 'name', 'category', 'optima_id',)
    search_fields = ['name', 'code', ]
    list_filter = ['category__name']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
