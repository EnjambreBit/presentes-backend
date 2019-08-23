from django.db import models

class LugarDelHecho(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")

    class Meta:
        ordering = ['nombre']
        db_table = 'lugares_del_hecho'
        verbose_name_plural = "Lugares del Hecho"

    class JSONAPIMeta:
        resource_name = 'lugares-del-hecho'

    def __str__(self):
        return self.nombre
