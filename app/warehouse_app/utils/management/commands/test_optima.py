from django.core.management.base import BaseCommand
from utils.utils import OptimaConnection
from utils.models import OptimaProduct

class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = OptimaConnection()
        for row in connection.execute_query(OptimaProduct.query):
            product = OptimaProduct(row, create=False)
            print(product)
