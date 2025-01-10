from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import mixins, viewsets, status, generics
from rest_framework import filters
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from .filters import GISFeatureFilter
from .models import SpeciesLocation
from .serializers import SpeciesLocationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import GISFeaturePagination
from .tasks import notify_admins_and_process_put_request

"""
    A viewset that provides the update operation for SpeciesLocation.
"""

class SpeciesLocationListView(generics.ListAPIView):
    queryset = SpeciesLocation.objects.all()
    serializer_class = SpeciesLocationSerializer
    pagination_class = GISFeaturePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = GISFeatureFilter
    permission_classes = [AllowAny,]
    search_fields = ['species_id', 'scientific_name', 'country', 'state_province', 'family', 'kingdom', 'genus']


# class GetAllSpeciesLocationViewSet(
#     mixins.ListModelMixin,
#     viewsets.GenericViewSet
# ):
#     http_method_names = ['get']
#     queryset = SpeciesLocation.objects.all()
#     serializer_class = SpeciesLocationSerializer
#     pagination_class = GISFeaturePagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_class = GISFeatureFilter
#     permission_classes = [AllowAny,]
#     search_fields = ['id', 'scientific_name', 'country', 'state_province', 'family', 'kingdom', 'genus']

"""
    A viewset that provides the update operation for SpeciesLocation.
"""
class SpeciesLocationRetreiveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = SpeciesLocation.objects.all()
    serializer_class = SpeciesLocationSerializer
    permission_classes = [IsAdminUser,]
    # TODO: add a rendere class to make response srid 4326
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    # def perform_update(self, serializer):
    #     serializer.save()
    # def retrieve(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #     except Http404:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     notify_admins_and_process_put_request.delay(request.data)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

class UpdateSpeciesLocationViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = SpeciesLocation.objects.all()
    serializer_class = SpeciesLocationSerializer
    permission_classes = [IsAdminUser,]

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        notification = [request.data, request.user.email]
        notify_admins_and_process_put_request.delay(notification)
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)
