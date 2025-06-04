from django.db import models

# Create your models here.
class ProductosTerceros(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField(default=1.0) 
    vendedor = models.IntegerField(null=True, blank=True)  # Campo para el ID del vendedor
  
    def __str__(self):
        return self.nombre

