from rest_framework import serializers
from presentes.models.provincias import Provincia
from rest_framework_json_api.relations import ResourceRelatedField
from presentes.serializers.paises import PaisSerializer

class ProvinciaSerializer(serializers.ModelSerializer):

    pais = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Provincia
        fields = ('id', 'nombre', 'sigla', 'pais')

    included_serializers = {
        'pais': PaisSerializer,
    }

    class JSONAPIMeta:
        resource_name = 'provincias'
        included_resources = ['pais',]
