# Generated by Django 2.2.1 on 2019-08-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0052_caso_descripcion_del_hecho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='email',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='referente',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
