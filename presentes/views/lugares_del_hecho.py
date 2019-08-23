from rest_framework import viewsets

from presentes.models.lugares_del_hecho import LugarDelHecho
from presentes.serializers.lugares_del_hecho import LugarDelHechoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class LugarDelHechoViewSet(viewsets.ModelViewSet):
    queryset = LugarDelHecho.objects.all()
    resource_name = 'lugares-del-hecho'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = LugarDelHechoSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
