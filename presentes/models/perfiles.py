import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Perfil(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")
    apellido = models.CharField(max_length=200, default="", help_text="")
    user = models.ManyToManyField(User, on_delete=models.CASCADE, default=None)
    grupos = models.ManyToManyField(Group, related_name="perfiles", default=None, blank=True)

    class Meta:
        ordering = ['-id']
        db_table = 'perfiles'
        verbose_name_plural = "perfiles"

    class JSONAPIMeta:
        resource_name = 'perfiles'

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

    def usuario(self):
        return self.user.username

    def email(self):
        return self.user.email
