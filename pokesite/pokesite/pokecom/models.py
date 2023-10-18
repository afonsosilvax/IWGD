from django.db import models

# Create your models here.
class Carta(models.Model):
    pokemon = models.CharField(max_length=200)
    raridade = models.CharField(max_length=200)
    colecao = models.CharField(max_length=200)
    imagem = models.ImageField(default="")
    preco = models.DecimalField(default="0.0", max_digits=7, decimal_places=2)
    id = models.BigAutoField(primary_key=True)

