# Generated by Django 2.2.1 on 2019-05-10 18:06

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0010_caso'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='fecha_del_hecho',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
