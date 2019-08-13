from rest_framework import serializers
from presentes.models.casos import Caso
from presentes.models.provincias import Provincia
from presentes.models.categorias import Categoria
from presentes.models.etiquetas import Etiqueta
from presentes.models.organizaciones import Organizacion
from presentes.models.estados_de_caso import EstadoDeCaso
from rest_framework_json_api.relations import ResourceRelatedField


class CasoSerializer(serializers.ModelSerializer):

    provincia = ResourceRelatedField(queryset=Provincia.objects, many=False, read_only=False)
    provincia_del_penal = ResourceRelatedField(queryset=Provincia.objects,many=False, read_only=False, allow_null=True, required=False)
    violencia_institucion_provincia = ResourceRelatedField(queryset=Provincia.objects,many=False, read_only=False, allow_null=True, required=False)
    categoria = ResourceRelatedField(queryset=Categoria.objects, many=False, read_only=False)
    etiquetas = ResourceRelatedField(queryset=Etiqueta.objects, many=True, read_only=False, allow_null=True, required=False)
    cj_organizaciones = ResourceRelatedField(queryset=Organizacion.objects, many=True, read_only=False, allow_null=True, required=False)
    denuncia_organizaciones = ResourceRelatedField(queryset=Organizacion.objects, many=True, read_only=False, allow_null=True, required=False)
    estado_de_publicacion = ResourceRelatedField(queryset=EstadoDeCaso.objects, many=False, read_only=False)
    imagen_url = serializers.SerializerMethodField()

    def get_imagen_url(self, object):
        if object.imagen:
            request = self.context.get('request')
            return request.build_absolute_uri(object.imagen.url)
        else:
            return None

    class Meta:
        model = Caso
        read_only_fields = [
        ]
        fields = [
            'id',
            'nombre',
            'apellido',
            'lugar_de_nacimiento',
            'edad',
            'fecha_del_hecho',
            'localidad',
            'provincia',
            'latitud',
            'longitud',
            'categoria',
            'etiquetas',
            'descripcion_del_hecho',
            'causa_de_la_muerte',
            'tenia_obra_social',
            'obra_social',
            'tiene_acceso_a_prestaciones_de_salud',
            'prestaciones_de_salud',
            'ocupacion',
            'estudios_cursados',
            'estaba_en_situacion_de_calle',
            'donde_vivia',
            'estaba_detenida',
            'desde_cuando_estaba_encerrada',
            'tenia_prision_preventiva',
            'titulo_de_la_causa_en_la_justicia',
            'nombre_del_penal',
            'localidad_del_penal',
            'provincia_del_penal',
            'prostitucion',
            'es_migrante',
            'pais_de_origen',
            'anio_de_llegada',
            'hay_denuncia',
            'fecha_de_denuncia',
            'ante_quien_se_hizo_la_denuncia',
            'por_que_no_denuncio',
            'la_denuncia_reconoce_genero',
            'denuncia_organizaciones',
            'hay_causa_judicial',
            'cj_titulo_de_la_causa',
            'cj_numero_de_la_causa',
            'cj_anio_de_inicio',
            'cj_donde_se_tramita',
            'cj_instancia',
            'cj_respetaron_nombre_de_ig',
            'cj_organismos_publicos',
            'cj_organizaciones',
            'cj_otrasOrganizaciones',
            'cj_cuenta_con_defensa',
            'cj_hay_informe_forense',
            'hubo_violencia_institucional',
            'violencia_institucion_nombre',
            'violencia_institucion_localidad',
            'violencia_institucion_provincia',
            'observaciones',
            'nombre_de_quien_brindo_informacion',
            'telefono_de_quien_brindo_informacion',
            'estado_de_publicacion',
            'link_de_nota',
            'copete',
            'calle',
            'como_fue_el_ataque',
            'hubo_victimas',
            'hay_registro_fotografico',
            'imagen_url',
        ]

    included_serializers = {
        'etiquetas': 'presentes.serializers.etiquetas.EtiquetaSerializer',
        'provincia': 'presentes.serializers.provincias.ProvinciaSerializer',
        'provincia_del_penal': 'presentes.serializers.provincias.ProvinciaSerializer',
        'violencia_institucion_provincia': 'presentes.serializers.provincias.ProvinciaSerializer',
        'categoria': 'presentes.serializers.categorias.CategoriaSerializer',
        'estado_de_publicacion': 'presentes.serializers.estados_de_caso.EstadoDeCasoSerializer',
        'cj_organizaciones': 'presentes.serializers.organizaciones.OrganizacionSerializer',
        'denuncia_organizaciones': 'presentes.serializers.organizaciones.OrganizacionSerializer'
    }

    class JSONAPIMeta:
        included_resources = [
            'categoria',
            'etiquetas',
            'provincia',
            'provincia_del_penal',
            'violencia_institucion_provincia',
            'cj_organizaciones'
            'denuncia_organizaciones',
            'estado_de_publicacion'
        ]
