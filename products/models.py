from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=50)
    price = models.IntegerField(verbose_name="Precio")
    information = models.TextField(verbose_name="Información", max_length=500)
    acquisition_date = models.DateTimeField(verbose_name="Fecha de adquisición")
    image = models.ImageField(verbose_name="Imagen", upload_to="products")
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['acquisition_date']

    def __str__(self):
        return self.name