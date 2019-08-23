from rest_framework import viewsets

from presentes.models.mecanicas_del_hecho import MecanicaDelHecho
from presentes.serializers.mecanicas_del_hecho import MecanicaDelHechoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class MecanicaDelHechoViewSet(viewsets.ModelViewSet):
    queryset = MecanicaDelHecho.objects.all()
    resource_name = 'mecanicas-del-hecho'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = MecanicaDelHechoSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
