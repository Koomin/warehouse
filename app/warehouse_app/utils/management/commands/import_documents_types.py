import logging
from django.core.management.base import BaseCommand
from utils.utils import OptimaConnection
from utils.models import OptimaDocumentType

logger = logging.getLogger()


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        counter = 0
        for idx, row in enumerate(connection.execute_query(OptimaDocumentType.query)):
            document_type = OptimaDocumentType(row)
            logger.info(f'{idx}. Created {document_type}')
            counter += 1
        logger.info(f'Created {counter} document types. Finishing.')
