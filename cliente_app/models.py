from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.PositiveBigIntegerField(max_length=10)
    correo=models.CharField(max_length=100)
    membresia=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    