from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SpeciesLocationListView, UpdateSpeciesLocationViewSet, SpeciesLocationRetreiveDestroyView

router = DefaultRouter()
router.register(r'update', UpdateSpeciesLocationViewSet, basename='update-species')
urlpatterns = [
    path('locations/', SpeciesLocationListView.as_view(), name='list-species'),
    path('<int:pk>/', SpeciesLocationRetreiveDestroyView.as_view(), name='view-destroy-species'),
]

urlpatterns += router.urls
