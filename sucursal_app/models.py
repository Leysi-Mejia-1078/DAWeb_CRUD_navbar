from django.db import models

# Create your models here.

class Sucursal(models.Model):
    id_sucursal=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.PositiveBigIntegerField(max_length=10)
    gerente=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    horario=models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre