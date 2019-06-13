from django.db import models
import datetime
from django.db.models.signals import post_save, m2m_changed
from presentes.models.provincias import Provincia

class Caso(models.Model):
    #Opciones
    SI = "SI"
    NO = "NO"
    NOSABE = "NS"
    OPCIONES_DENUNCIA = (
        (SI, 'Si'),
        (NO, 'No'),
        (NOSABE, 'No sabe'),
        ('NT', 'No se la tomaron')
    )
    OPCIONES_SI_NO = (
        (SI, 'Si'),
        (NO, 'No')
    )
    OPCIONES_PUBLICA_PRIVADA = (
        ('PU', 'Pública'),
        ('PR', 'Privada')
    )
    #Datos de la víctima
    nombre = models.CharField(max_length=200, default="", help_text="")
    apellido = models.CharField(max_length=200, null=True, blank=True, default="", help_text="")
    imagen = models.ImageField(default=None, null=True, blank=True)
    lugar_de_nacimiento = models.CharField(max_length=255, default="", blank=True, null=True, help_text="")
    edad = models.CharField(max_length=3, default="", blank=True, null=True, help_text="")
    prostitucion = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)

    #Es migrante
    es_migrante =  models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)

    pais_de_origen = models.CharField(max_length=200, default="",null=True, blank=True, help_text="")
    anio_de_llegada = models.CharField(max_length=4, default="",null=True, blank=True, help_text="")

    #Datos del hecho
    fecha_del_hecho = models.DateField(default=datetime.date.today)
    localidad = models.CharField(max_length=200, default="", help_text="")
    provincia = models.ForeignKey('Provincia', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=20,blank=True, null=True, default="", help_text="")
    longitud = models.CharField(max_length=20,blank=True, null=True, default="", help_text="")

    categoria = models.ForeignKey('Categoria', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField('Etiqueta', related_name="casos", default=None, blank=True)

    #Si es muerte
    #Travesticidio y transfemicidio
    causa_de_la_muerte = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    tenia_obra_social = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    obra_social = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    tiene_acceso_a_prestaciones_de_salud = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    prestaciones_de_salud = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    #Travesticidio y Travesticidio social
    ocupacion = models.CharField(max_length=200, null=True,default="", blank=True, help_text="")
    estudios_cursados = models.CharField(max_length=200, default="",null=True, blank=True, help_text="")
    estaba_en_situacion_de_calle = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    donde_vivia = models.CharField(max_length=200, default="",null=True, blank=True, help_text="")

    #Situación de encierro
    estaba_detenida = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    tenia_prision_preventiva = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    titulo_de_la_causa_en_la_justicia = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    nombre_del_penal = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    localidad_del_penal = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    provincia_del_penal = models.ForeignKey('Provincia', related_name="casos_penal", default=None, blank=True, null=True, on_delete=models.CASCADE)

    #Denuncia
    hay_denuncia = models.CharField(max_length=2, choices=OPCIONES_DENUNCIA, default=None, null=True, blank=True)
    fecha_de_denuncia = models.DateField(default=datetime.date.today, null=True, blank=True)
    ante_quien_se_hizo_la_denuncia = models.CharField(max_length=200, default="",null=True, blank=True, help_text="")
    por_que_no_denuncio = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    la_denuncia_reconoce_genero = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)

    #Causa judicial
    hay_causa_judicial = models.CharField(max_length=2, choices=OPCIONES_DENUNCIA, default=None, null=True, blank=True)
    cj_titulo_de_la_causa = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    cj_numero_de_la_causa = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    cj_anio_de_inicio = models.CharField(max_length=4, default="", null=True, blank=True, help_text="")
    cj_donde_se_tramita = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    cj_instancia = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    cj_respetaron_nombre_de_ig = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    cj_organismos_publicos = models.TextField(default="", null=True, blank=True, help_text="")
    cj_organizaciones = models.ManyToManyField('Organizacion', related_name="casos", default=None, blank=True)
    cj_cuenta_con_defensa = models.CharField(max_length=2, choices=OPCIONES_PUBLICA_PRIVADA, default=None, null=True, blank=True)
    cj_hay_informe_forense = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)

    #Violencia institucional
    hubo_violencia_institucional = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    violencia_institucion_nombre = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    violencia_institucion_localidad = models.CharField(max_length=200, default="", null=True, blank=True, help_text="")
    violencia_institucion_provincia = models.ForeignKey('Provincia', related_name="casos_violencia_institucional", default=None, blank=True, null=True, on_delete=models.CASCADE)

    observaciones = models.TextField(default="",null=True, blank=True, help_text="")

    #Ataques a lugares
    calle = models.CharField(max_length=250,null=True, default="", blank=True, help_text="")
    como_fue_el_ataque = models.TextField(default="",null=True, blank=True, help_text="")
    hubo_victimas = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    hay_registro_fotografico = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)

    #La informacion del formulario fue brindada por
    nombre_de_quien_brindo_informacion = models.CharField(max_length=200,null=True, default="", blank=True, help_text="")
    telefono_de_quien_brindo_informacion = models.CharField(max_length=200, default="",null=True, blank=True, help_text="")

    link_de_nota = models.CharField(max_length=250, null=True, default="", blank=True, help_text="")
    copete = models.TextField(default="", null=True, blank=True, help_text="")


    fecha_de_creacion = models.DateField(default=datetime.date.today)
    estado_de_publicacion = models.ForeignKey('EstadoDeCaso', related_name="casos", default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        db_table = 'casos'
        verbose_name_plural = "casos"

    class JSONAPIMeta:
        resource_name = 'casos'

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

    def _aplicar_provincia(self, nombre):
        self.provincia = Provincia.objects.get(nombre=nombre)

    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if created:
            instance.save()

    @classmethod
    def serializar_personalizado(kls, caso, build_absolute_uri):
        datos = {
            "id": caso.id,
            "nombreCompleto": caso.nombre_completo(),
        }

        if caso.imagen:
            datos['imagenUrl'] = build_absolute_uri(caso.imagen.url)

        return datos

post_save.connect(Caso.post_create, sender=Caso)
