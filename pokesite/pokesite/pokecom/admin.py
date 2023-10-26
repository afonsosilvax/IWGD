from django.contrib import admin
from .models import Carta, Carta_troca, Organizador, Torneio

# Register your models here.
@admin.register(Carta, Carta_troca, Organizador, Torneio)

class ModelAdmin(admin.ModelAdmin):
    pass
