# Generated by Django 5.1.1 on 2024-09-24 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_foto', models.URLField(max_length=256)),
                ('url_redireccion', models.URLField(max_length=256)),
            ],
            options={
                'verbose_name': 'Anuncio',
                'verbose_name_plural': 'Anuncios',
                'db_table': 'anuncios',
            },
        ),
        migrations.CreateModel(
            name='Pregunta_Frecuente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField()),
                ('respuesta', models.TextField()),
            ],
            options={
                'verbose_name': 'Pregunta_Frecuente',
                'verbose_name_plural': 'Preguntas_Frecuentes',
                'db_table': 'preguntas_frecuentes',
            },
        ),
    ]
