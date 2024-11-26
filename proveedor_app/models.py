from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_proveedor=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.PositiveBigIntegerField(max_length=10)
    correo=models.CharField(max_length=100)
    tipo_de_producto=models.CharField(max_length=50)
    tipo_de_entrega=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre