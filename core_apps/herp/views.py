from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import mixins, viewsets, status
from rest_framework import filters

from .filters import GISFeatureFilter
from .models import SpeciesLocation
from .serializers import SpeciesLocationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import GISFeaturePagination
from .tasks import notify_admins_and_process_put_request

"""
    A viewset that provides the update operation for SpeciesLocation.
"""
class GetAllSpeciesLocationViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    http_method_names = ['get']
    queryset = SpeciesLocation.objects.all()
    serializer_class = SpeciesLocationSerializer
    pagination_class = GISFeaturePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = GISFeatureFilter
    permission_classes = [AllowAny,]
    search_fields = ['id', 'scientific_name', 'country', 'state_province', 'family', 'kingdom', 'genus']

"""
    A viewset that provides the update operation for SpeciesLocation.
"""
class UpdateSpeciesLocationViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = SpeciesLocation.objects.all()
    serializer_class = SpeciesLocationSerializer
    permission_classes = [AllowAny,]
    # def update(self, request, *args, **kwargs):
    #     data = request.data
    #     notify_admins_and_process_put_request.delay(data)
    #     return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        notify_admins_and_process_put_request.delay(request.data)
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)
