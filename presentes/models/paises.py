from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")
    sigla = models.CharField(max_length=3, default="", help_text="")

    class Meta:
        ordering = ['-id']
        db_table = 'paises'
        verbose_name_plural = "paises"

    class JSONAPIMeta:
        resource_name = 'paises'

    def __str__(self):
        return "{} ({})".format(self.nombre, self.sigla)
