from django.db import models
from simple_history.models import HistoricalRecords


class WarehouseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
