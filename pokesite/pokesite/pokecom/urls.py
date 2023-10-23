from django.urls import path, include
from . import views

app_name = "pokecom"

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('register_comp', views.register_comp, name='register_comp'),
    path('login', views.loginview, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.fazlogout, name='logout'),
    path('fazer_upload', views.fazer_upload, name='fazer_upload'),
    path('criar_torneios', views.criar_torneios, name='criar_torneios'),
    path('torneios', views.torneios, name='torneios'),

    path('pesquisar', views.pesquisar, name='pesquisar'),
    path('vender', views.vender, name='vender'),
    path('trocar', views.trocar, name='trocar'),
    path('dispcarta', views.dispcarta, name='dispcarta'),
    path('pesuisar_troca', views.pesquisar_troca, name='pesquisar_troca'),
    ]