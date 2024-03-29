from rest_framework import viewsets, status
from rest_framework import permissions

from products.models import Product, Unit, ProductCategory, ProductAvailability
from products.api.serializers import ProductSerializer, UnitSerializer, ProductCategorySerializer, \
    ProductAvailabilitySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'


class ProductAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = ProductAvailability.objects.all()
    serializer_class = ProductAvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'
