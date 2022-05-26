from django.db import models

# Create your models here.

class producto(models.Model):
    Nombre=models.CharField(max_length=100, unique=True)
    Precio=models.CharField(max_length=250)
    Cantidad=models.IntegerField()
    Descripción =models.CharField(max_length=250)

    def __str__(self):
        return self.Nombre