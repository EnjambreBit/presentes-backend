# Generated by Django 2.2.1 on 2019-05-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0028_auto_20190530_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='edad',
            field=models.CharField(blank=True, default='', max_length=3, null=True),
        ),
    ]
