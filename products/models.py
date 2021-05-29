from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    precio = models.IntegerField(verbose_name="Precio")
    informacion = models.TextField(verbose_name="Informacion")
    fecha_adquisicion = models.DateTimeField(verbose_name="Fecha de adquisición")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="products")
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre