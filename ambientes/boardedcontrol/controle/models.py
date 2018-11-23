from django.db import models
from ambientes.models import Ambiente

# Create your models here.


class Rede(models.Model):
    ip = models.CharField(max_length=40)
    mascara = models.CharField(max_length=40)
    mac = models.CharField(max_length=40)
    ipGateway = models.CharField(max_length=40)


class Sensor(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    data = models.IntegerField()
    sampleRate = models.DecimalField(max_digits=4, decimal_places=4)


class Atuador(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    status = models.IntegerField()


class Mqtt(models.Model):
    ip = models.CharField(max_length=40)
    porta = models.IntegerField()

    def __str__(self):
        return self.ip


class Embarcado(models.Model):
    descricao = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    localizacao = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    tipo = models.IntegerField()
    firmware = models.CharField(max_length=30)
    rede = models.ForeignKey(Rede, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    mqtt = models.ForeignKey(Mqtt, on_delete=models.CASCADE)
    atuador = models.ForeignKey(Atuador, on_delete=models.CASCADE)
