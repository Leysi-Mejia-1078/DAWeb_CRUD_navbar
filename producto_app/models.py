from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    peso=models.DecimalField(max_digits=6,decimal_places=2)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    tamano=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre