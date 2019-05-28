from django.db import models

class EstadoDeCaso(models.Model):
  nombre = models.CharField(max_length=200, default="")

  class Meta:
      ordering = ['-id']
      db_table = 'estados-de-caso'
      verbose_name_plural = "Estados de Caso"

  class JSONAPIMeta:
      resource_name = 'estados-de-caso'

  def __str__(self):
      return "{}".format(self.nombre)
