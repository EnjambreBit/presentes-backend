import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Perfil(models.Model):
    nombre = models.CharField(max_length=200, default="", help_text="")
    apellido = models.CharField(max_length=200, default="", help_text="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
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

    def obtener_diccionario_de_permisos(self):
        todos_los_permisos = Permission.objects.exclude(name__startswith='Can')
        permisos_asignados = []

        for grupo in self.grupos.all():
            for permiso in grupo.permissions.all():
                permisos_asignados.append(permiso)

        permisos = {}

        for p in todos_los_permisos:
            if p in permisos_asignados:
                permisos[p.codename] = True
            else:
                permisos[p.codename] = False

        return permisos

    def es_admin(self):
        return self.obtener_diccionario_de_permisos().get('admin', False)

    def nombres_de_grupos(self):
        grupos = self.grupos.all()
        nombres = [grupo.name for grupo in grupos]
        return ", ".join(nombres)

    def tiene_permiso(self, permiso):
        return self.obtener_diccionario_de_permisos().get(permiso, False)

    @classmethod
    def serializar_personalizado(kls, perfil, build_absolute_uri):
        datos = {
            "id": perfil.id,
            "nombreCompleto": perfil.nombre_completo(),
        }

        return datos
