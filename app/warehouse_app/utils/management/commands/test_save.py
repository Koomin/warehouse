from django.core.management.base import BaseCommand
from documents.models import Document

class Command(BaseCommand):

    def handle(self, *args, **options):
        d = Document.objects.get(pk=25)
        d.save_to_optima()
