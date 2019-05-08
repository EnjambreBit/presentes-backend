# Generated by Django 2.2.1 on 2019-05-07 20:17

from django.db import migrations
from django.contrib.auth.models import User

def crear_usuario_administrador(apps, schema_editor):
    User.objects.create_superuser(username='admin', password='asdasd123', email='')

class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_usuario_administrador, migrations.RunPython.noop),
    ]