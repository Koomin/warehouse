from rest_framework import viewsets, status
from rest_framework import permissions

from stores.models import Store
from stores.api.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = []
