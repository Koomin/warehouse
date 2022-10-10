import pytest
import factory

from documents.api.serializers import DocumentTypeSerializer, DocumentSerializer
from tests.test_documents.factories import DocumentTypeFactory, DocumentFactory


@pytest.mark.django_db
class TestDocumentTypeSerializer:

    def test_serialize_model(self):
        document_type = DocumentTypeFactory()
        serializer = DocumentTypeSerializer(document_type)

        assert serializer.data

    def test_serialized_data(self):
        valid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=DocumentTypeFactory
        )
        serializer = DocumentTypeSerializer(data=valid_serialized_data)

        assert serializer.is_valid()
        assert serializer.errors == {}


@pytest.mark.django_db
class TestDocumentSerializer:

    def test_serialize_model(self):
        document = DocumentFactory()
        serializer = DocumentSerializer(document)

        assert serializer.data

    def test_serialized_data(self):
        d = DocumentFactory()
        valid_serialized_data = {
            'uuid': d.uuid,
            'optima_id': d.optima_id,
            'document_type': d.document_type.uuid,
            'optima_full_number': d.optima_full_number,
            'value_net': d.value_net,
            'value_gross': d.value_gross,
            'value_vat': d.value_vat,
            'source_store': d.source_store.uuid,
            'destination_store': d.destination_store.uuid,
            'document_group': d.document_group.uuid,
            'document_date': d.document_date,
            'document_creation_date': d.document_creation_date,
            'exported': d.exported,
            'realized': d.realized,
            'issued': d.issued
        }

        serializer = DocumentSerializer(data=valid_serialized_data)

        assert serializer.is_valid(raise_exception=True)
        assert serializer.errors == {}
