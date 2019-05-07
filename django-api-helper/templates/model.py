from django.db import models
#import datetime


class Modelo(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")
    #pais = models.ForeignKey('Pais', related_name="modelo_plural", default=None, null=True, on_delete=models.CASCADE)
    #fecha_de_creacion = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['-id']
        db_table = 'modelo_plural'
        verbose_name_plural = "modelo_plural"

    class JSONAPIMeta:
        resource_name = 'modelo_plural'

    def __str__(self):
        return self.nombre
