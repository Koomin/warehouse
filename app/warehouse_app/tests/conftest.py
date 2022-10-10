import pytest
from rest_framework.test import APIClient


from warehouse_auth.models import WarehouseUser


@pytest.mark.django_db
def create_user():
    user = WarehouseUser.objects.create(username='user', login_permission=True, is_active=True)
    user.set_password('password')
    user.save()


def api_authenticate(api_client):
    endpoint = '/api/v1/token/'
    response = api_client.post(endpoint, data={'username': 'user', 'password': 'password'})
    return response.data.get('access')


@pytest.fixture
def api_client():
    api_client = APIClient()
    create_user()
    token = api_authenticate(api_client)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api_client
