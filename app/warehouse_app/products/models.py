from django.db import models

from stores.models import Store
from warehouse.models import WarehouseModel


class Unit(WarehouseModel):
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.short_name}'


class ProductCategory(WarehouseModel):
    name = models.CharField(max_length=55, null=False, blank=False)
    product_code = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.product_code} - {self.name}'


class Product(WarehouseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=50, null=False, blank=False)
    pkwiu = models.CharField(max_length=50, default='')
    optima_id = models.PositiveIntegerField(null=False, blank=False)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=True, blank=False)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    retail_value = models.DecimalField(max_digits=12, decimal_places=4, default=0.0000)

    def __str__(self):
        return f'{self.code} - {self.name}'


class ProductAvailability(WarehouseModel):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=12, decimal_places=4, default=0.0000)
    value = models.DecimalField(max_digits=12, decimal_places=4, default=0.0000)
    unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.code} - {self.store.short_name} - {self.quantity} {self.unit.short_name}'

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.unit = self.product.unit
        super().save(*args, **kwargs)
