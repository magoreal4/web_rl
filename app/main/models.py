from django.db import models
from django.core.validators import FileExtensionValidator


class Banner(models.Model):
    titulo = models.CharField(max_length=20, unique=True)
    contenido = models.TextField(max_length=150)
    imagen = models.ImageField(upload_to='banner')
    visible = models.BooleanField(default=True, verbose_name="¿Visible?")

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self):
        return self.titulo


class Servicios(models.Model):
    titulo = models.CharField(max_length=80, unique=True)
    resumen = models.TextField(max_length=200, unique=True, null=True)
    contenido = models.TextField(max_length=1000, unique=True, null=True)
    imagen = models.ImageField(upload_to='servicios')
    orden = models.OrderBy
    visible = models.BooleanField(
        default=True, verbose_name="Visible en tarjetas?")
    icono = models.ImageField(
        upload_to='iconosServicios', unique=True, null=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo


class Logos(models.Model):
    titulo = models.CharField(max_length=15, unique=True)
    imagen = models.ImageField(upload_to='clientes')
    visible = models.BooleanField(default=True, verbose_name="¿Visible?")

    class Meta:
        verbose_name = 'logo'
        verbose_name_plural = 'logos'

    def __str__(self):
        return self.titulo