from warehouse_app.stores.models import Store
from warehouse_app.products.models import Product, Unit


class OptimaProduct:
    query = 'SELECT Twr_TwrId, Twr_Kod, Twr_Nazwa, Twr_JM, Twr_JMZ, Twr_JMPrzelicznikL, Twr_JMPrzelicznikM' \
            ' FROM CDN.Towary'

    def __init__(self, data_row, create=True):
        self.data_row = data_row
        self.optima_id = self.get_optima_id()
        self.optima_code = self.get_optima_code()
        self.optima_name = self.get_optima_name()
        self.optima_unit = self.get_optima_unit()
        self.optima_unit_collective = self.get_optima_unit_collective()
        self.optima_unit_converter = self.get_optima_unit_converter()
        self.optima_unit_converter_collective = self.get_optima_unit_converter_collective()
        if create:
            self.create_product()

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

    def get_or_create_unit(self):
        unit, created = Unit.objects.get_or_create(
            short_name=self.optima_unit
        )
        return unit

    def create_product(self):
        Product.objects.update_or_create(
            optima_id=self.optima_id,
            defaults={
                'name': self.optima_name,
                'code': self.optima_code,
                'unit': self.get_or_create_unit()
            }
        )


class OptimaStore:
    query = 'SELECT Mag_MagId, Mag_Symbol, Mag_Nazwa, Mag_Opis, Mag_Rejestr, Mag_NieAktywny FROM CDN.Magazyny'

    def __init__(self, data_row, create=True):
        self.data_row = data_row
        self.optima_id = self.get_optima_id()
        self.optima_short_name = self.get_optima_short_name()
        self.optima_name = self.get_optima_name()
        self.optima_description = self.get_optima_description()
        self.optima_register = self.get_optima_register()
        self.optima_inactive = self.get_optima_inactive()
        if create:
            self.create_store()

    def __str__(self):
        return self.optima_short_name

    def get_optima_id(self):
        return self.data_row[0]

    def get_optima_short_name(self):
        return self.data_row[1]

    def get_optima_name(self):
        return self.data_row[2]

    def get_optima_description(self):
        return self.data_row[3]

    def get_optima_register(self):
        return self.data_row[4]

    def get_optima_inactive(self):
        return self.data_row[5]

    def create_store(self):
        Store.objects.update_or_create(
            optima_id=self.optima_id,
            defaults={
                'short_name': self.optima_short_name,
                'name': self.optima_name,
                'description': self.optima_description,
                'register': self.optima_register,
                'status': self.optima_inactive
            }
        )
