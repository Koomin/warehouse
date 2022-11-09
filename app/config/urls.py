from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from documents.api.views import (DocumentViewSet,
                                 DocumentItemViewSet,
                                 DocumentTypeViewSet,
                                 OrderViewSet,
                                 OrderItemViewSet,
                                 )
from products.api.views import ProductViewSet, UnitViewSet, ProductCategoryViewSet, ProductAvailabilityViewSet
from stores.api.views import StoreViewSet
from warehouse_auth.api.authentication import TokenWithUserObtainPairView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'products-availability', ProductAvailabilityViewSet)
router.register(r'units', UnitViewSet)
router.register(r'product-category', ProductCategoryViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'document-item', DocumentItemViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-item', OrderItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenWithUserObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
