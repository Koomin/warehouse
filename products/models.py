from django.db import models
from simple_history.models import HistoricalRecords


class ProductCategory(models.Model):
    name = models.CharField(max_length=55)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
