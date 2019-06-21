from rest_framework import serializers
from presentes.models.archivos import Archivo
from rest_framework_json_api.relations import ResourceRelatedField


class ArchivoSerializer(serializers.ModelSerializer):

    caso = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Archivo
        fields = ('id', 'archivo', 'caso')

    included_serializers = {
        'caso': 'presentes.serializers.casos.CasoSerializer'
    }

    class JSONAPIMeta:
        included_resources = ['caso',]
