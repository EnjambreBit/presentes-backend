# Generated by Django 2.2.1 on 2019-05-21 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0012_auto_20190510_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='fecha_de_nacimiento',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='caso',
            name='lugar_de_nacimiento',
            field=models.CharField(default='', max_length=255),
        ),
    ]
