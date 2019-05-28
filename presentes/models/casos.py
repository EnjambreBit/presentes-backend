from django.db import models
import datetime
from django.db.models.signals import post_save, m2m_changed
from presentes.models.provincias import Provincia

class Caso(models.Model):
    #Datos de la víctima
    nombre = models.CharField(max_length=200, default="", help_text="")
    apellido = models.CharField(max_length=200, default="", help_text="")
    lugar_de_nacimiento = models.CharField(max_length=255, default="", help_text="")
    fecha_de_nacimiento = models.DateField(default=datetime.date.today)

    #Datos del hecho
    fecha_del_hecho = models.DateField(default=datetime.date.today)
    lugar_del_hecho = models.CharField(max_length=250, default="")
    localidad = models.CharField(max_length=200, default="", help_text="")
    provincia = models.ForeignKey('Provincia', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=20, default="", help_text="")
    longitud = models.CharField(max_length=20, default="", help_text="")

    categoria = models.ForeignKey('Categoria', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField('Etiqueta', related_name="casos", default=None, blank=True)

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
