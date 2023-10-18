from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse,HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Carta

# Create your views here.

def index(request):
    return render(request, "pokecom/index.html")

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username= request.POST.get('username'), password=request.POST.get('pswd'))
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return HttpResponse('Utilizador ou password incorretas')
    return render(request, 'pokecom/login.html')

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get('username'),email = request.POST.get('email'),password = request.POST.get('password') )
        user.save()
        return redirect('/')
    return render(request, 'pokecom/register.html',)

def home(request):
    return render(request, 'pokecom/home.html')

def fazlogout(request):
    logout(request)
    return render(request, 'pokecom/logout.html')

def fazer_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        pokemon_name = request.POST.get('nome_pokemon')
        raridade = request.POST.get('raridade')
        colecao = request.POST.get('colecao')
        preco = request.POST.get('preco')

        c = Carta(pokemon_name, raridade, colecao, myfile, preco)
        c.save()

        return render(request, 'pokecom/venda_form.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'pokecom/venda_form.html')






def pesquisar(request):
    return render(request, 'pokecom/pesquisar.html')

def vender(request):
    return render(request, 'pokecom/vender.html')

def trocar(request):
    return render(request, 'pokecom/trocar.html')

def dispcarta(request):
    return render(request, 'pokecom/troca_carta.html')

def pesquisar_troca(request):
    return render(request, 'pokecom/troca_pesq.html')
