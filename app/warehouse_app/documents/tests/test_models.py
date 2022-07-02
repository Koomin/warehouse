from django.test import TestCase

from documents.models import Document, DocumentType, DocumentItem
from products.models import Product, Unit
from stores.models import Store


class DocumentTest(TestCase):

    def __init__(self, *args):
        super().__init__(*args)
        self.unit = self.create_unit('szt')
        self.document_type = self.create_document_type(1, 312, 'MM', 'Przesunięcie międzymagazynowe',
                                                       '@nazwa/@numer/@rok', 1, True)
        self.source_store = self.create_store(1, '1', 'Source store', 'Description', 'Source', Store.ACTIVE)
        self.destination_store = self.create_store(2, '2', 'Destination store', 'Description', 'Destination',
                                                   Store.ACTIVE)

        self.first_product = self.create_product('Bread', 'BR', 123, self.unit, 5.7500)
        self.second_product = self.create_product('Doughnut', 'DG', 124, self.unit, 2.4500)
        self.document = self.create_document()
        self.first_item = self.create_document_item(self.document, self.first_product, 240, 1)
        self.second_item = self.create_document_item(self.document, self.second_product, 300, 2)

    def create_store(self, optima_id, short_name, name, description, register, status):
        return Store.objects.create(
            optima_id=optima_id,
            short_name=short_name,
            name=name,
            description=description,
            register=register,
            status=status
        )

    def create_document_type(self, optima_id, optima_class, short_name, name, numbering, type_id, is_active):
        return DocumentType.objects.create(optima_id=optima_id,
                                           optima_class=optima_class,
                                           short_name=short_name,
                                           name=name,
                                           numbering=numbering,
                                           type_id=type_id,
                                           is_active=is_active)

    def create_document(self):
        return Document.objects.create(
            document_type=self.document_type,
            value_vat=0.00,
            value_net=0.00,
            value_gross=0.00,
            source_store=self.source_store,
            destination_store=self.destination_store
        )

    def create_unit(self, short_name):
        return Unit.objects.create(short_name=short_name)

    def create_product(self, name, code, optima_id, unit, value):
        return Product.objects.create(
            name=name,
            code=code,
            optima_id=optima_id,
            unit=unit,
            value=value
        )

    def create_document_item(self, document, product, quantity, optima_id):
        return DocumentItem.objects.create(
            optima_id=optima_id,
            document=document,
            product=product,
            quantity=quantity
        )

    def test_document_type_creation(self):
        self.assertTrue(isinstance(self.document_type, DocumentType))
        self.assertEqual(self.document_type.__str__(), 'MM')

    def test_document_creation(self):
        self.assertTrue(isinstance(self.document, Document))
        self.assertEqual(self.document.__str__(), 'Przesunięcie międzymagazynowe - 2115.0000')
        self.assertEqual(self.document.value_net, 2115.00)
        self.assertEqual(self.document.value_gross, 2220.75)
        self.assertEqual(self.document.value_vat, 105.75)

    def test_document_item_creation(self):
        self.assertTrue(isinstance(self.first_item, DocumentItem))
        self.assertTrue(isinstance(self.second_item, DocumentItem))
        self.assertEqual(self.first_item.__str__(), 'MM - Bread - 1380.0000')
        self.assertEqual(self.second_item.__str__(), 'MM - Doughnut - 735.0000')
        self.assertEqual(self.first_item.net_price, 1380.00)
        self.assertEqual(self.second_item.net_price, 735.00)
        self.assertEqual(self.first_item.gross_price, 1449.00)
        self.assertEqual(self.second_item.gross_price, 771.75)
