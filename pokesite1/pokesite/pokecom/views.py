from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse,HttpResponseRedirect
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "pokecom/index.html")

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

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username= request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Utilizador ou password incorretas')
    return render(request, 'pokecom/login.html')

def criaruser(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get('username'),email = request.POST.get('email'),password = request.POST.get('password') )
        user.save()
        return redirect('/')
    return render(request, 'pokecom/criaruser.html',)

def fazlogout(request):
    logout(request)
    return redirect('/')



