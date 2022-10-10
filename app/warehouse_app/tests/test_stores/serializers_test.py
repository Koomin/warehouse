import factory

from stores.api.serializers import StoreSerializer
from tests.test_stores.factories import StoreFactory


class TestStoreSerializer:

    def test_serialize_model(self):
        store = StoreFactory.build()
        serializer = StoreSerializer(store)

        assert serializer.data

    def test_serialized_data(self):
        valid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=StoreFactory
        )
        serializer = StoreSerializer(data=valid_serialized_data)

        assert serializer.is_valid()
        assert serializer.errors == {}
