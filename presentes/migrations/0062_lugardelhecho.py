# Generated by Django 2.2.1 on 2019-08-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0061_auto_20190822_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='LugarDelHecho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'lugares_del_hecho',
                'db_table': 'lugares_del_hecho',
                'ordering': ['-id'],
            },
        ),
    ]
