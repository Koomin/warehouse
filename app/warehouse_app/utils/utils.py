import pyodbc
import logging
from django.conf import settings

logger = logging.getLogger()


class OptimaConnection:
    def __init__(self):
        try:
            self.cnxn = pyodbc.connect(
                'Driver={ODBC Driver 17 for SQL Server};'
                f"Server={settings.OPTIMA_DB['SERVER']};"
                f"Database={settings.OPTIMA_DB['DATABASE']};"
                f"uid={settings.OPTIMA_DB['UID']};"
                f"pwd={settings.OPTIMA_DB['PASSWORD']}",
                autocommit=False
            )
        except pyodbc.OperationalError:
            logger.warning('Connection refused')
            self.cnxn = None
            self.cursor = None
        else:
            self.cursor = self.cnxn.cursor()

    def execute_query(self, query: str):
        return self.cursor.execute(query).fetchall()
