# Generated by Django 5.1.1 on 2024-11-08 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_descuento_fin_alter_descuento_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 7, 20, 15, 19, 316359)),
        ),
        migrations.AlterField(
            model_name='descuento',
            name='inicio',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 7, 20, 15, 19, 316359)),
        ),
    ]
