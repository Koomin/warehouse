import decimal

import factory
from factory.fuzzy import FuzzyDecimal
from documents.models import Document, DocumentType, DocumentGroup
from tests.test_stores.factories import StoreFactory


class DocumentGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DocumentGroup

    uuid = factory.faker.Faker('uuid4')
    optima_id = factory.faker.Faker('pyint')
    name = factory.faker.Faker('name')


class DocumentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DocumentType

    uuid = factory.faker.Faker('uuid4')
    optima_id = factory.faker.Faker('pyint')
    optima_class = factory.faker.Faker('pyint')
    details_id = factory.faker.Faker('pyint')
    name = factory.faker.Faker('name')
    short_name = factory.lazy_attribute(lambda o: o.name[:2])
    numbering = factory.lazy_attribute(lambda o: f'{o.short_name}/$number/$year')
    type_id = factory.faker.Faker('pyint')
    is_active = factory.faker.Faker('pybool')


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Document

    uuid = factory.faker.Faker('uuid4')
    optima_id = factory.faker.Faker('pyint')
    document_type = factory.SubFactory(DocumentTypeFactory)
    optima_full_number = factory.lazy_attribute(lambda o: f'{o.document_type.short_name}/{o.optima_id}')
    value_net = FuzzyDecimal(1000, 20000.5)
    value_gross = factory.lazy_attribute(
        lambda o: decimal.Decimal(o.value_net * decimal.Decimal(1.05)).quantize(decimal.Decimal('.01'),
                                                                                rounding=decimal.ROUND_HALF_UP))
    value_vat = factory.lazy_attribute(
        lambda o: decimal.Decimal(o.value_gross - o.value_net).quantize(decimal.Decimal('.01'),
                                                                        rounding=decimal.ROUND_HALF_UP))
    source_store = factory.SubFactory(StoreFactory)
    destination_store = factory.SubFactory(StoreFactory)
    document_group = factory.SubFactory(DocumentGroupFactory)
    document_date = factory.faker.Faker('date_time')
    document_creation_date = factory.faker.Faker('date_time')
    exported = factory.faker.Faker('pybool')
    realized = factory.faker.Faker('pybool')
    issued = factory.faker.Faker('pybool')
