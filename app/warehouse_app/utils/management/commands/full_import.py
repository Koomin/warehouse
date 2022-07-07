from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        call_command('import_stores')
        call_command('import_products')
        call_command('import_documents_types')
        call_command('import_documents_groups')
        call_command('import_documents')
