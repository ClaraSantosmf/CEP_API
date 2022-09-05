from django.db import models

# Create your models here.


class Estado(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    sigla = models.CharField(max_length=8, unique=True)


class Cidade(models.Model):
    nome = models.CharField(max_length=128)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)


class Cep(models.Model):
    cep = models.CharField(max_length=8, unique=True)
    logradouro = models.CharField(max_length=256, null=True, blank=True)
    complemento = models.CharField(max_length=256, null=True, blank=True)
    bairro = models.CharField(max_length=256, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
