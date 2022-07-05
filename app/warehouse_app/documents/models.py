import decimal
import logging

from django.db import models, transaction

from utils.helpers import WarehouseDocument, WarehouseDocumentItem
from utils.utils import OptimaConnection
from products.models import Product
from stores.models import Store
from warehouse.models import WarehouseModel

logger = logging.getLogger()


class DocumentType(WarehouseModel):
    optima_id = models.PositiveIntegerField()
    optima_class = models.PositiveIntegerField()
    details_id = models.PositiveIntegerField(null=True, blank=True)
    short_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    numbering = models.CharField(max_length=255, null=False, blank=False)
    type_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name


class Document(WarehouseModel):
    optima_id = models.PositiveIntegerField(null=True, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, null=False, blank=False)
    optima_full_number = models.CharField(max_length=255, null=True, blank=True)
    value_net = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0.00)
    value_vat = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0.00)
    value_gross = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0.00)
    source_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False, blank=False,
                                     related_name='document_source')
    destination_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True,
                                          related_name='document_destination')
    exported = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.document_type.name} - {self.value_net}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @transaction.atomic
    def save_to_optima(self):
        connection = OptimaConnection()
        cursor = connection.cursor
        saved = False
        if cursor:
            try:
                optima_document = WarehouseDocument(self, cursor)
                optima_id = optima_document.export_to_optima()
                self.optima_id = optima_id
                self.save()
                for idx, document_item in enumerate(self.document_items.all().order_by('pk')):
                    optima_document_item = WarehouseDocumentItem(idx + 1, document_item, cursor)
                    optima_document_item_id = optima_document_item.export_to_optima()
                    document_item.optima_id = optima_document_item_id
                    document_item.save()
            except Exception:
                connection.cnxn.rollback()
            else:
                self.exported = True
                self.optima_full_number = optima_document.number_string
                self.save()
                connection.cnxn.commit()
                saved = True
            finally:
                cursor.close()
                connection.cnxn.close()
        return saved

    def recalculate_values(self):
        value_net = 0
        for document_item in self.document_items.all():
            value_net += document_item.net_price

        self.value_net = value_net
        self.value_gross = decimal.Decimal(self.value_net * decimal.Decimal(1.05)).quantize(
            decimal.Decimal('.0100'), rounding=decimal.ROUND_HALF_UP)
        self.value_vat = self.value_gross - self.value_net
        self.save()


class DocumentItem(WarehouseModel):
    optima_id = models.PositiveIntegerField(null=True, blank=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='document_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False,
                                related_name='document_items')
    quantity = models.DecimalField(max_digits=12, decimal_places=4, null=False, blank=False)
    net_price = models.DecimalField(max_digits=12, decimal_places=4, null=False, blank=True)
    gross_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=False)

    def __str__(self):
        return f'{self.document.document_type.short_name} - {self.product.name} - {self.net_price}'

    def save(self, *args, **kwargs):
        self.net_price = decimal.Decimal(self.product.value * self.quantity).quantize(
            decimal.Decimal('.0100'), rounding=decimal.ROUND_HALF_UP)
        self.gross_price = decimal.Decimal(self.net_price * decimal.Decimal(1.05)).quantize(
            decimal.Decimal('.0100'), rounding=decimal.ROUND_HALF_UP)
        super().save(*args, **kwargs)
        self.document.recalculate_values()


class DocumentGroup(WarehouseModel):
    optima_id = models.PositiveIntegerField(null=False, blank=False)
    document_type = models.ManyToManyField(DocumentType, null=False, blank=False)
    name = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return f'{self.optima_id} - {self.name}'
