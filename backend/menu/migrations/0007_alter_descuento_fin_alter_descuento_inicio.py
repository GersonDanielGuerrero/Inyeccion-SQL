# Generated by Django 5.1.1 on 2024-10-18 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_categoria_url_foto_alter_descuento_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 18, 16, 4, 25, 656483)),
        ),
        migrations.AlterField(
            model_name='descuento',
            name='inicio',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 18, 16, 4, 25, 656483)),
        ),
    ]