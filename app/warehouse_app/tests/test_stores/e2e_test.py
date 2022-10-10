import pytest
import json

from stores.models import Store
from tests.test_stores.factories import StoreFactory

@pytest.mark.django_db
class TestStoreEndpoints:

    endpoint = '/api/store/'

    def test_list(self, api_client):
        StoreFactory.create_batch(5)
        print(api_client.credentials)
        response = api_client.get(self.endpoint)
        print(response.data)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5

    def test_create(self, api_client):
        store = StoreFactory.build()
        expected_json = {
            'optima_id': store.optima_id,
            'short_name': store.short_name,
            'name': store.name,
            'description': store.description,
            'register': store.register,
            'status': store.status
        }
        response = api_client.post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        expected_json['uuid'] = json.loads(response.content).get('uuid')
        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client):
        store = StoreFactory()
        expected_json = {
            'uuid': store.uuid,
            'optima_id': store.optima_id,
            'short_name': store.short_name,
            'name': store.name,
            'description': store.description,
            'register': store.register,
            'status': store.status
        }
        response = api_client.get(f'{self.endpoint}{store.uuid}/')
        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, api_client):
        old_store = StoreFactory()
        new_store = StoreFactory.build()
        store_dict = {
            'optima_id': new_store.optima_id,
            'short_name': new_store.short_name,
            'register': new_store.register,
        }
        response = api_client.put(
            f'{self.endpoint}{old_store.uuid}/',
            data=store_dict,
            format='json'
        )
        store_dict['uuid'] = old_store.uuid
        store_dict['name'] = old_store.name
        store_dict['description'] = old_store.description
        store_dict['status'] = old_store.status
        assert response.status_code == 200
        assert json.loads(response.content) == store_dict

    def test_delete(self, api_client):
        store = StoreFactory()
        response = api_client.delete(f'{self.endpoint}{store.uuid}/')
        assert response.status_code == 204
        assert Store.objects.all().count() == 0
