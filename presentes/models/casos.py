from django.db import models
import datetime

class Caso(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")
    apellido = models.CharField(max_length=200, default="", help_text="")
    localidad = models.CharField(max_length=200, default="", help_text="")
    provincia = models.ForeignKey('Provincia', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=20, default="", help_text="")
    longitud = models.CharField(max_length=20, default="", help_text="")
    categoria = models.ForeignKey('Categoria', related_name="casos", default=None, null=True, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField('Etiqueta', related_name="casos", default=None, blank=True)
    fecha_del_hecho = models.DateField(default=datetime.date.today)
    fecha_de_creacion = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['-id']
        db_table = 'casos'
        verbose_name_plural = "casos"

    class JSONAPIMeta:
        resource_name = 'casos'

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
