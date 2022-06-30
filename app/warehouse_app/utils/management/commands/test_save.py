from django.core.management.base import BaseCommand
from warehouse_app.documents.models import Document

class Command(BaseCommand):

    def handle(self, *args, **options):
        d = Document.objects.get(pk=23)
        d.save_to_optima()
