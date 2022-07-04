import logging
from django.core.management.base import BaseCommand

from documents.models import DocumentType
from utils.utils import OptimaConnection
from utils.models import OptimaDocument, OptimaDocumentItem

logger = logging.getLogger()


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        counter = 0
        for document_type in DocumentType.objects.filter(is_active=True).values_list('pk', flat=True):
            for idx, row in enumerate(connection.execute_query(OptimaDocument.query.format(document_type))):
                document = OptimaDocument(row)
                for row_item in connection.execute_query(OptimaDocumentItem.query.format(document.optima_id)):
                    OptimaDocumentItem(row_item)
                logger.info(f'{idx}. Created {document}')
                counter += 1
            logger.info(f'Created {counter} document types. Finishing.')
