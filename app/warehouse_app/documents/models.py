from django.db import models

from warehouse_app.warehouse.models import WarehouseModel


class DocumentType(WarehouseModel):
    optima_id = models.PositiveIntegerField()
    optima_class = models.PositiveIntegerField()
    short_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=True)
