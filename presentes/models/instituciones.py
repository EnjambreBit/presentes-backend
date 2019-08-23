from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")

    class Meta:
        ordering = ['nombre']
        db_table = 'instituciones'
        verbose_name_plural = "Instituciones"

    class JSONAPIMeta:
        resource_name = 'instituciones'

    def __str__(self):
        return self.nombre
