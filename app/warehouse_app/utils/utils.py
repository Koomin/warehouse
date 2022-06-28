import pyodbc
from django.conf import settings


class OptimaConnection:
    def __init__(self):
        self.cnxn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            f"Server={settings.OPTIMA_DB['SERVER']};"
            f"Database={settings.OPTIMA_DB['DATABASE']};"
            f"uid={settings.OPTIMA_DB['UID']};"
            f"pwd={settings.OPTIMA_DB['PASSWORD']}",
            autocommit=False
        )
        self.cursor = self.cnxn.cursor()

    def execute_query(self, query: str):
        return self.cursor.execute(query).fetchall()
