# Generated by Django 2.2.1 on 2019-06-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0044_auto_20190612_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='latitud',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='caso',
            name='longitud',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
