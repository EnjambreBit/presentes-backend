# Generated by Django 2.2.1 on 2019-06-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0035_auto_20190603_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='ocupacion',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]