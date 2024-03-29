import logging
from django.core.management.base import BaseCommand
from utils.utils import OptimaConnection
from utils.models import OptimaProduct

logger = logging.getLogger()


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        counter = 0
        for idx, row in enumerate(connection.execute_query(OptimaProduct.query)):
            product = OptimaProduct(row)
            logger.info(f'{idx}. Created {product}')
            counter += 1
        logger.info(f'Created {counter} products. Finishing.')
