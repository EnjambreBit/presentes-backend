from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")

    class Meta:
        ordering = ['-id']
        db_table = 'categorias'
        verbose_name_plural = "categorias"

    class JSONAPIMeta:
        resource_name = 'categorias'

    def __str__(self):
        return self.nombre
