from django.contrib import admin

from warehouse_app.documents.models import DocumentType
from warehouse_app.warehouse.admin import WarehouseAdmin


@admin.register(DocumentType)
class DocumentTypeAdmin(WarehouseAdmin):
    list_display = ('short_name', 'name', 'optima_class', 'optima_id', 'is_active')
    list_filter = ['is_active']
    search_fields = ['optima_class', 'name', 'short_name']
