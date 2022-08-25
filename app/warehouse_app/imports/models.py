from django.core.management import call_command
from django.db import models

from utils.tasks import async_imports
from warehouse.models import WarehouseModel


class Import(WarehouseModel):
    IMPORT_PRODUCTS = 'import_products'
    IMPORT_DOCUMENTS_TYPES = 'import_documents_types'
    IMPORT_DOCUMENTS = 'import_documents'
    IMPORT_DOCUMENTS_GROUPS = 'import_documents_groups'
    IMPORT_STORES = 'import_stores'
    FULL_IMPORT = 'full_import'
    IMPORT_TYPES = (
        (IMPORT_STORES, 'Import stores'),
        (IMPORT_DOCUMENTS, 'Import documents'),
        (IMPORT_PRODUCTS, 'Import products'),
        (IMPORT_DOCUMENTS_TYPES, 'Import documents types'),
        (IMPORT_DOCUMENTS_GROUPS, 'Import documents groups'),
        (FULL_IMPORT, 'Full import'),
    )
    method = models.CharField(choices=IMPORT_TYPES, max_length=120, null=False, blank=False)

    def __str__(self):
        return self.method

    def save(self, *args):
        super().save(*args)
        async_imports.apply_async(kwargs={'command': self.method}, retry=False)
