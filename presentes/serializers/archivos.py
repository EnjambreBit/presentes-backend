from rest_framework import serializers
from presentes.models.archivos import Archivo
from rest_framework_json_api.relations import ResourceRelatedField
from presentes.serializers.casos import CasoSerializer


class ArchivoSerializer(serializers.ModelSerializer):

    caso = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Archivo
        fields = ('id', 'archivo', 'caso')

    included_serializers = {
        'caso': CasoSerializer
    }

    class JSONAPIMeta:
        resource_name = 'archivos'
        included_resources = ['caso',]
