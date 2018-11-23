from django.db import models


# Create your models here.


class Ambiente(models.Model):
    area = models.CharField(max_length=5)
    bloco = models.CharField(max_length=15)
    sala = models.CharField(max_length=15)


class Recurso(models.Model):
    nome = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    serial = models.CharField(max_length=30, unique=True)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)


