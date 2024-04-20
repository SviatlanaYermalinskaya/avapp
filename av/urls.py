from rest_framework import routers
from av.api import BrandViewSet


router = routers.DefaultRouter()
router.register('api/brand', BrandViewSet, 'brand')

urlpatterns = router.urls
