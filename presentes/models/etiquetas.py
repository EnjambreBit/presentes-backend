from django.db import models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")

    class Meta:
        ordering = ['-id']
        db_table = 'etiquetas'
        verbose_name_plural = "etiquetas"

    class JSONAPIMeta:
        resource_name = 'etiquetas'

    def __str__(self):
        return self.nombre
