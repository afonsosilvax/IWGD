from django.contrib import admin
from .models import Carta, Carta_troca, Organizador, Torneio, Classificacao

# Register your models here.
@admin.register(Carta, Carta_troca, Organizador, Torneio, Classificacao)

class ModelAdmin(admin.ModelAdmin):
    pass
