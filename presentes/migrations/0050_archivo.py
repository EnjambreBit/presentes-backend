# Generated by Django 2.2.1 on 2019-06-21 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0049_caso_cj_otrasorganizaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos/')),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivos', to='presentes.Caso')),
            ],
            options={
                'verbose_name_plural': 'archivos',
                'db_table': 'archivos',
                'ordering': ['-id'],
            },
        ),
    ]