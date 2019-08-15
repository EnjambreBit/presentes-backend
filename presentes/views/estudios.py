from rest_framework import viewsets

from presentes.models.estudios import Estudio
from presentes.serializers.estudios import EstudioSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class EstudioViewSet(viewsets.ModelViewSet):
    queryset = Estudio.objects.all()
    resource_name = 'estudios'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = EstudioSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
