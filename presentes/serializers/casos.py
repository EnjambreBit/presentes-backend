from rest_framework import serializers
from presentes.models.casos import Caso
from rest_framework_json_api.relations import ResourceRelatedField


class CasoSerializer(serializers.ModelSerializer):

    provincia = ResourceRelatedField(many=False, read_only=True)
    categoria = ResourceRelatedField(many=False, read_only=True)
    etiquetas = ResourceRelatedField(many=True, read_only=True)

    class Meta:
        model = Caso
        fields = ('id', 'nombre', 'apellido', 'lugar_de_nacimiento','fecha_de_nacimiento', 'localidad', 'provincia', 'fecha_del_hecho', 'latitud', 'longitud', 'categoria', 'etiquetas')

    included_serializers = {
        'etiquetas': 'presentes.serializers.etiquetas.EtiquetaSerializer',
        'provincia': 'presentes.serializers.provincias.ProvinciaSerializer',
        'categoria': 'presentes.serializers.categorias.CategoriaSerializer'
    }

    class JSONAPIMeta:
        included_resources = ['categoria', 'etiquetas', 'provincia']
