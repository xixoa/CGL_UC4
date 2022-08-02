from django.db import models

class Estudiante(models.Model):
    codigo = models.CharField(max_length=10)
    DNI = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apepat = models.CharField(max_length=80)
    apemat = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    estado = models.CharField(max_length=1)