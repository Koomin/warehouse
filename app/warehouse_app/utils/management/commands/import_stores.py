import logging
from django.core.management.base import BaseCommand
from warehouse_app.utils.utils import OptimaConnection
from warehouse_app.utils.models import OptimaStore

logger = logging.getLogger()


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        counter = 0
        for idx, row in enumerate(connection.execute_query(OptimaStore.query)):
            store = OptimaStore(row)
            logger.info(f'{idx}. Created {store}')
            counter += 1
        logger.info(f'Created {counter} stores. Finishing.')
