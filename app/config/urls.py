from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from documents.views import DocumentViewSet, DocumentItemViewSet
from products.views import ProductViewSet, UnitViewSet, ProductCategoryViewSet
from stores.views import StoreViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'units', UnitViewSet)
router.register(r'product-category', ProductCategoryViewSet)
router.register(r'store', StoreViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'document-item', DocumentItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
