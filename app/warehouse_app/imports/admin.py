from django.contrib import admin

from imports.models import Import
from warehouse.admin import WarehouseAdmin


@admin.register(Import)
class ImportAdmin(WarehouseAdmin):
    list_display = ('method', 'created')
