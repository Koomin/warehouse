from django.contrib import admin

from documents.actions import export_to_optima
from documents.models import DocumentType, Document, DocumentItem
from warehouse.admin import WarehouseAdmin


@admin.register(DocumentType)
class DocumentTypeAdmin(WarehouseAdmin):
    list_display = ('short_name', 'name', 'optima_class', 'optima_id', 'is_active')
    list_filter = ['is_active']
    search_fields = ['optima_class', 'name', 'short_name']


class DocumentItemInline(admin.TabularInline):
    model = DocumentItem
    autocomplete_fields = ['product', ]


@admin.register(Document)
class DocumentAdmin(WarehouseAdmin):
    list_display = (
        'optima_full_number', 'value_net', 'value_vat', 'value_gross', 'optima_id', 'document_type', 'source_store',
        'destination_store')
    inlines = [DocumentItemInline, ]
    autocomplete_fields = ['document_type', 'source_store', 'destination_store']
    list_filter = ['document_type', ]
    actions = (export_to_optima,)
