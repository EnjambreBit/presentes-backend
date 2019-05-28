from rest_framework import serializers
from presentes.models.casos import Caso
from presentes.models.provincias import Provincia
from presentes.models.categorias import Categoria
from presentes.models.etiquetas import Etiqueta
from presentes.models.estados_de_caso import EstadoDeCaso
from rest_framework_json_api.relations import ResourceRelatedField


class CasoSerializer(serializers.ModelSerializer):

    provincia = ResourceRelatedField(queryset=Provincia.objects, many=False, read_only=False)
    categoria = ResourceRelatedField(queryset=Categoria.objects, many=False, read_only=False)
    etiquetas = ResourceRelatedField(many=True, read_only=True)
    estado_de_publicacion = ResourceRelatedField(queryset=EstadoDeCaso.objects, many=False, read_only=False)

    class Meta:
        model = Caso
        read_only_fields = [
            'lugar_de_nacimiento',
            'fecha_de_nacimiento'
        ]
        fields = [
            'id',
            'nombre',
            'apellido',
            'lugar_de_nacimiento',
            'fecha_de_nacimiento',
            'lugar_del_hecho',
            'localidad',
            'provincia',
            'fecha_del_hecho',
            'latitud',
            'longitud',
            'categoria',
            'etiquetas',
            'estado_de_publicacion'
        ]

    included_serializers = {
        'etiquetas': 'presentes.serializers.etiquetas.EtiquetaSerializer',
        'provincia': 'presentes.serializers.provincias.ProvinciaSerializer',
        'categoria': 'presentes.serializers.categorias.CategoriaSerializer',
        'estado_de_publicacion': 'presentes.serializers.estados_de_caso.EstadoDeCasoSerializer'
    }

    class JSONAPIMeta:
        included_resources = [
            'categoria',
            'etiquetas',
            'provincia',
            'estado_de_publicacion'
        ]
