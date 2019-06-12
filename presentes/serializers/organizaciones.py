from rest_framework import serializers
from presentes.models.organizaciones import Organizacion
from presentes.models.provincias import Provincia
from rest_framework_json_api.relations import ResourceRelatedField


class OrganizacionSerializer(serializers.ModelSerializer):

    provincia = ResourceRelatedField(queryset=Provincia.objects, many=False, read_only=False)

    class Meta:
        model = Organizacion
        fields = (
            'id',
            'nombre',
            'direccion',
            'telefono',
            'email',
            'descripcion',
            'localidad',
            'provincia'
        )

    included_serializers = {
        'provincia': 'presentes.serializers.provincias.ProvinciaSerializer'
    }

    class JSONAPIMeta:
        included_resources = ['provincia']
