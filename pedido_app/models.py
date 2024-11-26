from django.db import models

# Create your models here.

class Pedido(models.Model):
    id_pedido=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    fecha=models.CharField(max_length=8)
    nombre_cliente=models.CharField(max_length=100)
    producto=models.CharField(max_length=200)
    estado=models.CharField(max_length=100)
    cantidad_total=models.DecimalField(max_digits=10,decimal_places=2)
    metodo_entrega=models.CharField(max_length=100)

    def __str__(self):
        return self.estado