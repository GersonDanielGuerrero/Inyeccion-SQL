# Generated by Django 5.1.1 on 2024-11-25 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_anuncio_url_redireccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='url_foto',
            new_name='imagen',
        ),
    ]
