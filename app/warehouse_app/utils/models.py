from documents.models import DocumentType, Document, DocumentItem
from stores.models import Store
from products.models import Product, Unit


class OptimaProduct:
    query = 'SELECT Towary.Twr_TwrId, Towary.Twr_Kod, Towary.Twr_Nazwa, Towary.Twr_JM, Towary.Twr_JMZ, ' \
            'Towary.Twr_JMPrzelicznikL, Towary.Twr_JMPrzelicznikM, Ceny.TwC_Wartosc ' \
            'FROM CDN.Towary as Towary ' \
            'INNER JOIN CDN.TwrCeny as Ceny ON Towary.Twr_TwrId=Ceny.TwC_TwrID ' \
            'WHERE Ceny.TwC_Typ=1'

    def __init__(self, data_row, create=True):
        self.data_row = data_row
        self.optima_id = self.get_optima_id()
        self.optima_code = self.get_optima_code()
        self.optima_name = self.get_optima_name()
        self.optima_unit = self.get_optima_unit()
        self.optima_value = self.get_optima_value()
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

    def get_optima_value(self):
        return self.data_row[7]

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
                'value': self.optima_value,
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


class OptimaDocumentType:
    query = 'SELECT DDf_DDfID, DDf_Klasa, DDf_Symbol, DDf_Nazwa, DDf_Numeracja FROM CDN.DokDefinicje'

    def __init__(self, data_row, create=True):
        self.data_row = data_row
        self.optima_id = self.get_optima_id()
        self.optima_short_name = self.get_optima_short_name()
        self.optima_name = self.get_optima_name()
        self.optima_class = self.get_optima_class()
        self.optima_numbering = self.get_optima_numbering()
        if create:
            self.create_document_type()

    def __str__(self):
        return self.optima_name

    def get_optima_id(self):
        return self.data_row[0]

    def get_optima_class(self):
        return self.data_row[1]

    def get_optima_short_name(self):
        return self.data_row[2]

    def get_optima_name(self):
        return self.data_row[3]

    def get_optima_numbering(self):
        return self.data_row[4].replace('@brak/', '').replace('/@brak', '')

    def create_document_type(self):
        DocumentType.objects.update_or_create(
            optima_id=self.optima_id,
            defaults={
                'short_name': self.optima_short_name,
                'name': self.optima_name,
                'optima_class': self.optima_class,
                'numbering': self.optima_numbering
            }
        )


class OptimaDocument:
    query = 'SELECT TrN_TrNID, TrN_DDfId, TrN_NumerPelny, TrN_RazemNetto, TrN_RazemVat,TrN_RazemBrutto, TrN_MagZrdId,' \
            ' TrN_MagDocId FROM CDN.TraNag WHERE TrN_DDfId = {0}'

    def __init__(self, data_row, create=True):
        self.data_row = data_row
        self.optima_id = self.get_optima_id()
        self.document_type = self.get_document_type()
        self.optima_full_number = self.get_optima_full_number()
        self.value_net = self.get_value_net()
        self.value_vat = self.get_value_vat()
        self.value_gross = self.get_value_gross()
        self.source_store = self.get_source_store()
        self.destination_store = self.get_destination_store()
        if create:
            self.create_document()

    def __str__(self):
        return self.optima_full_number

    def get_optima_id(self):
        return self.data_row[0]

    def get_document_type(self):
        return DocumentType.objects.get(optima_id=self.data_row[1])

    def get_optima_full_number(self):
        return self.data_row[2]

    def get_value_net(self):
        return self.data_row[3]

    def get_value_vat(self):
        return self.data_row[4]

    def get_value_gross(self):
        return self.data_row[5]

    def get_source_store(self):
        try:
            store = Store.objects.get(optima_id=self.data_row[6])
        except Store.DoesNotExist:
            store = None
        return store

    def get_destination_store(self):
        try:
            store = Store.objects.get(optima_id=self.data_row[7])
        except Store.DoesNotExist:
            store = None
        return store

    def create_document(self):
        Document.objects.update_or_create(
            optima_id=self.optima_id,
            defaults={
                'document_type': self.document_type,
                'optima_full_number': self.optima_full_number,
                'value_net': self.value_net,
                'value_vat': self.value_vat,
                'value_gross': self.value_gross,
                'source_store': self.source_store,
                'destination_store': self.destination_store,
                'exported': True
            }
        )


class OptimaDocumentItem:
    query = 'SELECT TrE_TrEID, TrE_TrNId, TrE_TwrId, TrE_Ilosc,' \
            'TrE_WartoscNetto,TrE_WartoscBrutto FROM CDN.TraElem WHERE TrE_TrNId = {0}'

    def __init__(self, data_row, create=True):
        self.data_row = data_row
        self.optima_id = self.get_optima_id()
        self.document = self.get_document()
        self.product = self.get_product()
        self.quantity = self.get_quantity()
        self.net_price = self.get_net_price()
        self.gross_price = self.get_gross_price()

        if create:
            self.create_document_item()

    def __str__(self):
        return self.product

    def get_optima_id(self):
        return self.data_row[0]

    def get_document(self):
        return Document.objects.get(optima_id=self.data_row[1])

    def get_product(self):
        return Product.objects.get(optima_id=self.data_row[2])

    def get_quantity(self):
        return self.data_row[3]

    def get_net_price(self):
        return self.data_row[4]

    def get_gross_price(self):
        return self.data_row[5]

    def create_document_item(self):
        DocumentItem.objects.update_or_create(
            optima_id=self.optima_id,
            defaults={
                'document': self.document,
                'product': self.product,
                'quantity': self.quantity,
                'net_price': self.net_price,
                'gross_price': self.gross_price
            }
        )
