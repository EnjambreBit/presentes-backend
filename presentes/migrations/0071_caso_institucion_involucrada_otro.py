# Generated by Django 2.2.1 on 2019-08-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0070_caso_institucion_involucrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='institucion_involucrada_otro',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
