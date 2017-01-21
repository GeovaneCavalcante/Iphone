from django.db import models

class Enviados(models.Model):
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    identidicador = (" E-mail registrados")
    def __str__(self):
        return (self.identidicador)