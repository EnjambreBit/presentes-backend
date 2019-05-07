from rest_framework import viewsets

from presentes.models.perfiles import Perfil
from presentes.serializers.perfiles import PerfilSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    resource_name = 'perfiles'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = PerfilSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
