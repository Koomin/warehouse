from django.db import models

# Create your models here.


class OptimaProduct:

    query = 'SELECT Twr_TwrId, Twr_Kod, Twr_Nazwa, Twr_JM, Twr_JMZ, Twr_JMPrzelicznikL, Twr_JMPrzelicznikM' \
            ' FROM CDN.Towary'

    def __init__(self, data_row):
        self.data_row = data_row
        self.optima_id = self.get_optima_id()
        self.optima_code = self.get_optima_code()
        self.optima_name = self.get_optima_name()
        self.optima_unit = self.get_optima_unit()
        self.optima_unit_collective = self.get_optima_unit_collective()
        self.optima_unit_converter = self.get_optima_unit_converter()
        self.optima_unit_converter_collective = self.get_optima_unit_converter_collective()

    def __str__(self):
        return f'{self.optima_id} {self.optima_name} - {self.optima_code},' \
               f' {self.optima_unit} / {self.optima_unit_converter}'

    def get_optima_id(self):
        return self.data_row[0]

    def get_optima_code(self):
        return self.data_row[1]

    def get_optima_name(self):
        return self.data_row[2]

    def get_optima_unit(self):
        return self.data_row[3]

    def get_optima_unit_collective(self):
        return self.data_row[4]

    def get_optima_unit_converter(self):
        return self.data_row[5]

    def get_optima_unit_converter_collective(self):
        return self.data_row[6]
