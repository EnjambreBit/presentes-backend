# Generated by Django 2.2.1 on 2019-05-29 19:57

from django.db import migrations
from django.contrib.auth.models import Group

def crear_grupo_administrador(apps, schema_editor):
    Group.objects.create(name="Administrador")

class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0025_auto_20190529_1136'),
    ]

    operations = [
        migrations.RunPython(crear_grupo_administrador, migrations.RunPython.noop),
    ]