from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from documents.views import DocumentViewSet, DocumentItemViewSet, DocumentTypeViewSet
from products.views import ProductViewSet, UnitViewSet, ProductCategoryViewSet
from stores.views import StoreViewSet
from warehouse.authentication import TokenWithUserObtainPairView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'units', UnitViewSet)
router.register(r'product-category', ProductCategoryViewSet)
router.register(r'store', StoreViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'document-item', DocumentItemViewSet)
router.register(r'document-types', DocumentTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenWithUserObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
