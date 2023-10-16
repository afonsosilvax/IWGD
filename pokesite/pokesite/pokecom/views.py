from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse,HttpResponseRedirect
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "pokecom/index.html")

def loginview(request):
    print('loginview')
    if request.method == 'POST':
        user = authenticate(request, username= request.POST.get('username'), password=request.POST.get('password'))
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
