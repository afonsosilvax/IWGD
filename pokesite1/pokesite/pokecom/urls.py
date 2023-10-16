from django.urls import path, include
from . import views

app_name = "pokecom"
urlpatterns = [
    path('', views.index, name='index'),
    path('pesquisar', views.pesquisar, name='pesquisar'),
    path('vender', views.vender, name='vender'),
    path('trocar', views.trocar, name='trocar'),
    path('dispcarta', views.dispcarta, name='dispcarta'),
    path('pesuisar_troca', views.pesquisar_troca, name='pesquisar_troca'),
    path('login', views.loginview, name='login'),
    path('criaruser', views.criaruser, name='criaruser'),
    path('logout', views.fazlogout, name = 'logout'),
    ]