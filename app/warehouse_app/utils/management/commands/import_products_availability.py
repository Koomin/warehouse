import logging
from django.core.management.base import BaseCommand

from products.models import Product
from stores.models import Store
from utils.utils import OptimaConnection
from utils.models import OptimaProductAvailability

logger = logging.getLogger()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--products', nargs='+', type=int)
        parser.add_argument('--stores', nargs='+', type=int)

    def handle(self, *args, **options):
        connection = OptimaConnection()
        counter = 0
        stores = Store.objects.all() if not options.get('stores') else Store.objects.filter(
            pk__in=options.get('stores'))
        products = Product.objects.all() if not options.get('products') else Product.objects.filter(
            pk__in=options.get('products'))
        for store in stores:
            for product in products:
                query = OptimaProductAvailability.query.format(product.optima_id, store.optima_id)
                for idx, row in enumerate(connection.execute_query(query)):
                    product = OptimaProductAvailability(row, product, store)
                    logger.info(f'{idx}. Created {product}')
                    counter += 1
        logger.info(f'Created {counter} products. Finishing.')
