# Generated by Django 2.2.1 on 2019-05-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0031_auto_20190530_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='cj_cuenta_con_defensa',
            field=models.CharField(blank=True, choices=[('PU', 'Pública'), ('PR', 'Privada')], default=None, max_length=2, null=True),
        ),
    ]