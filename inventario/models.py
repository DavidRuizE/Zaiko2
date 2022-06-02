from django.db import models

# Create your models here.

class producto(models.Model):
    Nombre=models.CharField(max_length=100, unique=True)
    PrecioCompra=models.IntegerField(default=0)
    PrecioVenta=models.IntegerField(default=0)
    Cantidad=models.IntegerField()
    Descripción =models.CharField(max_length=250)
    Vendido=models.BooleanField(default=False)
    CantidadVendida=models.IntegerField(default=0)
    Ganancia=models.IntegerField(default=0)

    def __str__(self):
        return self.Nombre