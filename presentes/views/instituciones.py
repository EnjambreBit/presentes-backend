from rest_framework import viewsets

from presentes.models.instituciones import Institucion
from presentes.serializers.instituciones import InstitucionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    resource_name = 'instituciones'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = InstitucionSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
