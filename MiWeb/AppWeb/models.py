from django.db import models

# Create your models here.

class Familiares(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()

class Viajes(models.Model):

    pais = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    ultima_visita = models.DateField()

    

