from django.contrib import admin

from stores.models import Store
from warehouse.admin import WarehouseAdmin


@admin.register(Store)
class StoreAdmin(WarehouseAdmin):
    list_display = ('short_name', 'name', 'optima_id', 'status')
    search_fields = ['short_name']
    list_filter = ['status']
