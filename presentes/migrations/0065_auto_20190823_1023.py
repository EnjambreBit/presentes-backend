# Generated by Django 2.2.1 on 2019-08-23 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0064_espacioprivado'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='espacio_privado',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casos', to='presentes.EspacioPrivado'),
        ),
        migrations.AddField(
            model_name='caso',
            name='espacio_privado_otro',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
