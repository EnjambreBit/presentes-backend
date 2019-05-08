from rest_framework import serializers
from presentes.models.organizaciones import Organizacion
from rest_framework_json_api.relations import ResourceRelatedField


class OrganizacionSerializer(serializers.ModelSerializer):

    provincia = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Organizacion
        fields = ('id', 'nombre', 'direccion', 'telefono', 'provincia')

    included_serializers = {
        'provincia': 'presentes.serializers.provincia.ProvinciaSerializer'
    }

    class JSONAPIMeta:
        included_resources = ['participaciones', 'provincia']
