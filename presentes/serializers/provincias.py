from rest_framework import serializers
from presentes.models.provincias import Provincia
from rest_framework_json_api.relations import ResourceRelatedField


class ProvinciaSerializer(serializers.ModelSerializer):

    pais = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Provincia
        fields = ('id', 'nombre', 'sigla', 'pais')

    included_serializers = {
        'pais': 'presentes.serializers.paises.PaisSerializer'
    }

    class JSONAPIMeta:
        included_resources = ['pais',]
