from django.core.management.base import BaseCommand
from warehouse_app.utils.utils import OptimaConnection


class Command(BaseCommand):

    def handle(self):
        connection = OptimaConnection()
        for row in connection.execute_query('SELECT * FROM CDN.Towary'):
            print(row)