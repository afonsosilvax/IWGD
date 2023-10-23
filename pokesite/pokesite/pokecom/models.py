from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Carta(models.Model):
    pokemon = models.CharField(max_length=200)
    raridade = models.CharField(max_length=200)
    colecao = models.CharField(max_length=200)
    imagem = models.ImageField(default="")
    preco = models.DecimalField(default="0.0", max_digits=7, decimal_places=2)
    id = models.BigAutoField(primary_key=True)

class Organizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_org = models.CharField(max_length=200)

class Torneio(models.Model):
    nome_torneio = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    loja = models.CharField(max_length=200)
    nome_organizador = models.CharField(max_length=200)
    data = models.DateTimeField()
    premio = models.IntegerField(default="0")
    part = models.CharField(max_length=1000000)
    num_part = models.PositiveIntegerField(default="0")
    id = models.BigAutoField(primary_key=True)
