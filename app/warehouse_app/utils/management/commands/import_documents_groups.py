import logging
from django.core.management.base import BaseCommand

from utils.utils import OptimaConnection
from utils.models import OptimaDocumentGroup

logger = logging.getLogger()


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        for idx, row in enumerate(connection.execute_query(OptimaDocumentGroup.query)):
            document_group = OptimaDocumentGroup(row)
            logger.info(f'{idx}. Created {document_group}')
