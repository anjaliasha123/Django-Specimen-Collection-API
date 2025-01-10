from rest_framework.routers import DefaultRouter
from .views import GetAllSpeciesLocationViewSet, UpdateSpeciesLocationViewSet

router = DefaultRouter()
router.register(r'locations', GetAllSpeciesLocationViewSet, basename='list-species')
router.register(r'update', UpdateSpeciesLocationViewSet, basename='update-species')
urlpatterns = router.urls
