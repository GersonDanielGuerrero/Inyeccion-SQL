# Generated by Django 5.1.1 on 2024-11-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_alter_venta_producto_ingredientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito_producto',
            name='seleccionado',
            field=models.BooleanField(default=True),
        ),
    ]
