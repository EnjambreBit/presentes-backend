from rest_framework import serializers
from presentes.models.casos import Caso
from presentes.models.provincias import Provincia
from presentes.models.categorias import Categoria
from presentes.models.etiquetas import Etiqueta
from presentes.models.organizaciones import Organizacion
from presentes.models.estados_de_caso import EstadoDeCaso
from presentes.models.estudios import Estudio
from presentes.models.lugares_del_hecho import LugarDelHecho
from presentes.models.espacios_privados import EspacioPrivado
from presentes.models.mecanicas_del_hecho import MecanicaDelHecho
from presentes.models.instituciones import Institucion
from rest_framework_json_api.relations import ResourceRelatedField

from presentes.serializers.provincias import ProvinciaSerializer
from presentes.serializers.categorias import CategoriaSerializer
from presentes.serializers.etiquetas import EtiquetaSerializer
from presentes.serializers.organizaciones import OrganizacionSerializer
from presentes.serializers.estados_de_caso import EstadoDeCasoSerializer
from presentes.serializers.estudios import EstudioSerializer
from presentes.serializers.lugares_del_hecho import LugarDelHechoSerializer
from presentes.serializers.espacios_privados import EspacioPrivadoSerializer
from presentes.serializers.mecanicas_del_hecho import MecanicaDelHechoSerializer
from presentes.serializers.instituciones import InstitucionSerializer

class CasoSerializer(serializers.ModelSerializer):

    provincia = ResourceRelatedField(queryset=Provincia.objects, many=False, read_only=False)
    provincia_del_penal = ResourceRelatedField(queryset=Provincia.objects,many=False, read_only=False, allow_null=True, required=False)
    violencia_institucion_provincia = ResourceRelatedField(queryset=Provincia.objects,many=False, read_only=False, allow_null=True, required=False)
    categoria = ResourceRelatedField(queryset=Categoria.objects, many=False, read_only=False)
    etiquetas = ResourceRelatedField(queryset=Etiqueta.objects, many=True, read_only=False, allow_null=True, required=False)
    cj_organizaciones = ResourceRelatedField(queryset=Organizacion.objects, many=True, read_only=False, allow_null=True, required=False)
    denuncia_organizaciones = ResourceRelatedField(queryset=Organizacion.objects, many=True, read_only=False, allow_null=True, required=False)
    estado_de_publicacion = ResourceRelatedField(queryset=EstadoDeCaso.objects, many=False, read_only=False)
    que_estudios_tiene = ResourceRelatedField(queryset=Estudio.objects, many=False, read_only=False, allow_null=True, required=False)
    donde_ocurrio_el_hecho = ResourceRelatedField(queryset=LugarDelHecho.objects, many=False, read_only=False, allow_null=True, required=False)
    espacio_privado = ResourceRelatedField(queryset=EspacioPrivado.objects, many=False, read_only=False, allow_null=True, required=False)
    mecanica_del_hecho = ResourceRelatedField(queryset=MecanicaDelHecho.objects, many=False, read_only=False, allow_null=True, required=False)
    institucion_involucrada = ResourceRelatedField(queryset=Institucion.objects, many=False, read_only=False, allow_null=True, required=False)

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
            'donde_ocurrio_el_hecho',
            'espacio_privado',
            'espacio_privado_otro',
            'la_victima_conocia_al_victimario',
            'mecanica_del_hecho',
            'mecanica_del_hecho_otro',
            'causa_de_la_muerte',
            'tenia_obra_social',
            'obra_social',
            'tiene_acceso_a_prestaciones_de_salud',
            'prestaciones_de_salud',
            'ocupacion',
            'estudios_cursados',
            'que_estudios_tiene',
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
            'institucion_involucrada',
            'institucion_involucrada_otro',
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
        'etiquetas': EtiquetaSerializer,
        'provincia': ProvinciaSerializer,
        'provincia_del_penal': ProvinciaSerializer,
        'violencia_institucion_provincia': ProvinciaSerializer,
        'categoria': CategoriaSerializer,
        'estado_de_publicacion': EstadoDeCasoSerializer,
        'cj_organizaciones': OrganizacionSerializer,
        'denuncia_organizaciones': OrganizacionSerializer,
        'que_estudios_tiene': EstudioSerializer,
        'donde_ocurrio_el_hecho': LugarDelHechoSerializer,
        'espacio_privado': EspacioPrivadoSerializer,
        'mecanica_del_hecho': MecanicaDelHechoSerializer,
        'institucion_involucrada': InstitucionSerializer
    }

    class JSONAPIMeta:
        resource_name = 'casos'
        included_resources = [
            'categoria',
            'etiquetas',
            'provincia',
            'provincia_del_penal',
            'violencia_institucion_provincia',
            'cj_organizaciones'
            'denuncia_organizaciones',
            'estado_de_publicacion',
            'que_estudios_tiene',
            'donde_ocurrio_el_hecho',
            'espacio_privado',
            'mecanica_del_hecho',
            'institucion_involucrada'
        ]
