# Generated by Django 3.2.6 on 2021-09-04 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20, unique=True)),
                ('contenido', models.TextField(max_length=150)),
                ('imagen', models.ImageField(upload_to='banner')),
                ('visible', models.BooleanField(default=True, verbose_name='¿Visible?')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15, unique=True)),
                ('imagen', models.ImageField(upload_to='clientes')),
                ('visible', models.BooleanField(default=True, verbose_name='¿Visible?')),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logos',
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, unique=True)),
                ('resumen', models.TextField(max_length=200, null=True, unique=True)),
                ('contenido', models.TextField(max_length=1000, null=True, unique=True)),
                ('imagen', models.ImageField(upload_to='servicios')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible en tarjetas?')),
                ('icono', models.ImageField(null=True, unique=True, upload_to='iconosServicios')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
    ]