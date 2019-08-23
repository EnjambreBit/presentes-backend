from django.db import models

class EspacioPrivado(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")

    class Meta:
        ordering = ['nombre']
        db_table = 'espacios_privados'
        verbose_name_plural = "Espacios Privados"

    class JSONAPIMeta:
        resource_name = 'espacios-privados'

    def __str__(self):
        return self.nombre
