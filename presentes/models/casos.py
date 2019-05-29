from django.db import models
import datetime
from django.db.models.signals import post_save, m2m_changed
from presentes.models.provincias import Provincia

class Caso(models.Model):
    #Opciones
    SI = "SI"
    NO = "NO"
    NOSABE = "NS"
    OPCIONES_SI_NO_NOSABE = (
        (SI, 'Si'),
        (NO, 'No'),
        (NOSABE, 'No sabe'),
    )
    OPCIONES_SI_NO = (
        (SI, 'Si'),
        (NO, 'No')
    )
    #Datos de la víctima
    nombre = models.CharField(max_length=200, default="", help_text="")
    apellido = models.CharField(max_length=200, default="", help_text="")
    lugar_de_nacimiento = models.CharField(max_length=255, default="", blank=True, null=True, help_text="")
    edad = models.CharField(max_length=3, default="", help_text="")


    #Datos del hecho
    fecha_del_hecho = models.DateField(default=datetime.date.today)
    localidad = models.CharField(max_length=200, default="", help_text="")
    provincia = models.ForeignKey('Provincia', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=20, default="", help_text="")
    longitud = models.CharField(max_length=20, default="", help_text="")

    categoria = models.ForeignKey('Categoria', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField('Etiqueta', related_name="casos", default=None, blank=True)

    #Si es muerte
    causa_de_la_muerte = models.CharField(max_length=200, default="", blank=True, help_text="")

    #Es migrante
    es_migrante =  models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)
    pais_de_origen = models.CharField(max_length=200, default="", blank=True, help_text="")
    anio_de_llegada = models.CharField(max_length=4, default="", blank=True, help_text="")

    #Denuncia
    hay_denuncia = models.CharField(max_length=2, choices=OPCIONES_SI_NO_NOSABE, default=None, null=True, blank=True)
    fecha_de_denuncia = models.DateField(default=datetime.date.today, null=True, blank=True)
    ante_quien_se_hizo_la_denuncia = models.CharField(max_length=200, default="", blank=True, help_text="")
    por_que_no_denuncio = models.CharField(max_length=200, default="", blank=True, help_text="")
    la_denuncia_reconoce_genero = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default=None, null=True, blank=True)



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

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if created:
            instance.save()

post_save.connect(Caso.post_create, sender=Caso)
