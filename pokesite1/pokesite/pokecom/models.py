from django.db import models

# Create your models here.
class carta(models.Model):
    Pokemon = models.CharField(max_length=200)
    Raridade = models.CharField(max_length=200)
    Coleção = models.CharField(max_length=200)