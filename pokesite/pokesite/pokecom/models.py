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
    nome_organizador = models.ForeignKey(Organizador, on_delete=models.RESTRICT)
    data = models.DateTimeField()
    premio = models.DecimalField(default="0.0", max_digits=7, decimal_places=2)
    num_part = models.PositiveIntegerField(default="0")
