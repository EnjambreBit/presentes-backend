from django.db import models

class Archivo(models.Model):
    caso = models.ForeignKey('Caso', on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to="archivos/")

    class Meta:
        ordering = ['-id']
        db_table = 'archivos'
        verbose_name_plural = "archivos"

    class JSONAPIMeta:
        resource_name = 'archivos'

    def __str__(self):
        return "{}".format(self.archivo)
