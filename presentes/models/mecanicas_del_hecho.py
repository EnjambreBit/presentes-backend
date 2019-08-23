from django.db import models

class MecanicaDelHecho(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")

    class Meta:
        ordering = ['-id']
        db_table = 'mecanicas_del_hecho'
        verbose_name_plural = "Mécanicas del hecho"

    class JSONAPIMeta:
        resource_name = 'mecanicas-del-hecho'

    def __str__(self):
        return self.nombre
