from django.contrib import admin
from .models import Carta, Organizador, Torneio

# Register your models here.
@admin.register(Carta, Organizador, Torneio)

class ModelAdmin(admin.ModelAdmin):
    pass
