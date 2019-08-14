from django.db import models

class Organizacion(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")
    referente = models.CharField(max_length=200, default="", help_text="", blank=True, null=True)
    direccion = models.CharField(max_length=200, default="", help_text="", blank=True, null=True)
    localidad = models.CharField(max_length=200, default="", help_text="")
    telefono = models.CharField(max_length=200, default="", help_text="")
    email = models.CharField(max_length=200, default="", help_text="", blank=True, null=True)
    descripcion = models.TextField(default="", help_text="")
    provincia = models.ForeignKey('Provincia', related_name="organizaciones", default=None, null=True, on_delete=models.CASCADE)

    website = models.CharField(max_length=255, default="", help_text="", blank=True, null=True)
    facebook = models.CharField(max_length=255, default="", help_text="", blank=True, null=True)
    twitter = models.CharField(max_length=255, default="", help_text="", blank=True, null=True)
    instagram = models.CharField(max_length=255, default="", help_text="", blank=True, null=True)
    youtube = models.CharField(max_length=255, default="", help_text="", blank=True, null=True)


    class Meta:
        ordering = ['-id']
        db_table = 'organizaciones'
        verbose_name_plural = "organizaciones"

    class JSONAPIMeta:
        resource_name = 'organizaciones'

    def __str__(self):
        return "{} ({})".format(self.nombre, self.provincia)
