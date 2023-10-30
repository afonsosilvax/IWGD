from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Carta(models.Model):
    pokemon = models.CharField(max_length=200)
    raridade = models.CharField(max_length=200)
    colecao = models.CharField(max_length=200)
    subtipo = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    imagem = models.ImageField(default="")
    preco = models.DecimalField(default="0.0", max_digits=7, decimal_places=2)
    vendedor = models.CharField(max_length=200)
    id_api = models.CharField(max_length=200)
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

class Carta_troca(models.Model):
    pokemon = models.CharField(max_length=200)
    raridade = models.CharField(max_length=200)
    colecao = models.CharField(max_length=200)
    subtipo = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    imagem = models.ImageField(default="")
    preco = models.DecimalField(default="0.0", max_digits=7, decimal_places=2)
    vendedor = models.CharField(max_length=200)
    trade = models.CharField(max_length=200)
    id_api = models.CharField(max_length=200)
    id = models.BigAutoField(primary_key=True)

class Classificacao(models.Model):
    user_name = models.CharField(max_length=200)
    rating = models.DecimalField(default="2.5", max_digits=3, decimal_places=2)
    vendedor_name = models.CharField(max_length=200)
    comentario = models.CharField(default="", max_length=800)
