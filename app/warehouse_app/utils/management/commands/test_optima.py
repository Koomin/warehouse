from django.core.management.base import BaseCommand
from warehouse_app.utils.utils import OptimaConnection
from warehouse_app.utils.models import OptimaProduct

class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        for row in connection.execute_query(OptimaProduct.query):
            product = OptimaProduct(row, create=False)
            print(product)
