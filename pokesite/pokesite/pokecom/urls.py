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
    path('troca_form', views.troca_form, name='troca_form'),
    path('criar_torneios', views.criar_torneios, name='criar_torneios'),
    path('torneios', views.torneios, name='torneios'),
    path('procurar', views.procurar, name='procurar'),
    path('conf_compra', views.conf_compra, name='conf_compra'),
    path('procurar_troca', views.procurar_troca, name='procurar_troca'),
    path('conf_troca', views.conf_troca, name='conf_troca'),
    ]