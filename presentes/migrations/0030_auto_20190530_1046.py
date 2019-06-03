# Generated by Django 2.2.1 on 2019-05-30 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0029_auto_20190530_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='cj_violencia_institucion_provincia',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casos_cj_violencia', to='presentes.Provincia'),
        ),
        migrations.AlterField(
            model_name='caso',
            name='provincia_del_penal',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casos_penal', to='presentes.Provincia'),
        ),
    ]