from django.db import models

from warehouse_app.stores.models import Store
from warehouse_app.warehouse.models import WarehouseModel


class DocumentType(WarehouseModel):
    optima_id = models.PositiveIntegerField()
    optima_class = models.PositiveIntegerField()
    short_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    numbering = models.CharField(max_length=255, null=False, blank=False)
    type_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Document(WarehouseModel):
    optima_id = models.PositiveIntegerField(null=True, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, null=False, blank=False)
    optima_full_number = models.CharField(max_length=255, null=True, blank=True)
    value_net = models.DecimalField(max_digits=12, decimal_places=2)
    value_vat = models.DecimalField(max_digits=12, decimal_places=2)
    value_gross = models.DecimalField(max_digits=12, decimal_places=2)
    source_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False, blank=False, related_name='document_source')
    destination_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False, blank=False, related_name='document_destination')
