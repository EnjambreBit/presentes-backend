from django.db import models

class Estudio(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")

    class Meta:
        ordering = ['-id']
        db_table = 'estudios'
        verbose_name_plural = "estudios"

    class JSONAPIMeta:
        resource_name = 'estudios'

    def __str__(self):
        return "{}".format(self.nombre)
