# Generated by Django 2.2.1 on 2019-05-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0015_caso_lugar_del_hecho'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacion',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='organizacion',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
    ]
