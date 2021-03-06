# Generated by Django 2.2.1 on 2019-06-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0041_caso_estaba_detenida'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='calle',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='caso',
            name='como_fue_el_ataque',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='caso',
            name='hay_registro_fotografico',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], default=None, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='caso',
            name='hubo_victimas',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], default=None, max_length=2, null=True),
        ),
    ]
