from django.db import models
from warehouse.models import WarehouseModel


class ProductCategory(WarehouseModel):
    name = models.CharField(max_length=55, null=False, blank=False)
    product_code = models.CharField(max_length=255, null=False, blank=False)


class Product(WarehouseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=50, null=False, blank=False)
    optima_id = models.IntegerField(null=False, blank=False)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True)
