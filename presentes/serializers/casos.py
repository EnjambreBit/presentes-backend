from rest_framework import serializers
from presentes.models.casos import Caso
from presentes.models.provincias import Provincia
from presentes.models.categorias import Categoria
from presentes.models.etiquetas import Etiqueta
from rest_framework_json_api.relations import ResourceRelatedField


class CasoSerializer(serializers.ModelSerializer):

    provincia = ResourceRelatedField(queryset=Provincia.objects, many=False, read_only=False)
    categoria = ResourceRelatedField(queryset=Categoria.objects, many=False, read_only=False)
    etiquetas = ResourceRelatedField(many=True, read_only=True)

    class Meta:
        model = Caso
        fields = [
            'id',
            'nombre',
            'apellido',
            'lugar_de_nacimiento',
            'fecha_de_nacimiento',
            'localidad',
            'provincia',
            'fecha_del_hecho',
            'latitud',
            'longitud',
            'categoria',
            'etiquetas'
        ]

    included_serializers = {
        'etiquetas': 'presentes.serializers.etiquetas.EtiquetaSerializer',
        'provincia': 'presentes.serializers.provincias.ProvinciaSerializer',
        'categoria': 'presentes.serializers.categorias.CategoriaSerializer'
    }

    class JSONAPIMeta:
        included_resources = [
            'categoria',
            'etiquetas',
            'provincia'
        ]
