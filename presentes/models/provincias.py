from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")
    sigla = models.CharField(max_length=4, default="", help_text="")
    pais = models.ForeignKey('Pais', related_name="provincias", default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        db_table = 'provincias'
        verbose_name_plural = "provincias"

    class JSONAPIMeta:
        resource_name = 'provincias'

    def __str__(self):
        return "{} ({})".format(self.nombre, self.sigla)
