# Generated by Django 2.2.1 on 2019-06-04 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentes', '0037_auto_20190604_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caso',
            old_name='link_a_nota',
            new_name='link_de_nota',
        ),
    ]
