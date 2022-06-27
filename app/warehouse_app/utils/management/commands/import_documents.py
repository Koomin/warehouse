import logging
from django.core.management.base import BaseCommand
from warehouse_app.utils.utils import OptimaConnection
from warehouse_app.utils.models import OptimaDocument, OptimaDocumentItem

logger = logging.getLogger()


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        counter = 0
        for document_type in [20, 27]:
            for idx, row in enumerate(connection.execute_query(OptimaDocument.query.format(document_type))):
                document = OptimaDocument(row)
                for row_item in connection.execute_query(OptimaDocumentItem.query.format(document.optima_id)):
                    OptimaDocumentItem(row_item)
                logger.info(f'{idx}. Created {document}')
                counter += 1
            logger.info(f'Created {counter} document types. Finishing.')
