from django.db import models

# Create your models here.
from warehouse_app.warehouse.models import WarehouseModel


class Store(WarehouseModel):
    ACTIVE = 0
    INACTIVE = 1
    STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    )
    optima_id = models.PositiveIntegerField()
    short_name = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    register = models.CharField(max_length=50, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=ACTIVE)
