from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse,HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from .models import Carta, Organizador, Torneio, Carta_troca
import pokemontcgsdk


# Create your views here.

def index(request):
    return render(request, "pokecom/index.html")

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username= request.POST.get('username'), password=request.POST.get('pswd'))
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return HttpResponse('Utilizador ou password incorretas')
    return render(request, 'pokecom/login.html')

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get('username'),email = request.POST.get('email'),password = request.POST.get('pswd'))
        user.save()
        return redirect('/')
    return render(request, 'pokecom/register.html')

def register_comp(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get('username'),email = request.POST.get('email'),password = request.POST.get('pswd'))
        user.save()

        comp = Organizador(user=user, nome_org=request.POST.get('emp'))
        comp.save()

        return redirect('/')
    return render(request, 'pokecom/register_comp.html')

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

        pokemon_name = request.POST.get('nome_pokemon')
        raridade = request.POST.get('raridade')
        colecao = request.POST.get('colecao')
        estado = request.POST.get('estado')
        preco = request.POST.get('preco')
        vend = request.user.username

        c = Carta(pokemon_name, raridade, colecao, estado, filename, preco, vend)
        c.save()

        return render(request, 'pokecom/venda_form.html')
    return render(request, 'pokecom/venda_form.html')

def troca_form(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        pokemon_name = request.POST.get('nome_pokemon')
        raridade = request.POST.get('raridade')
        colecao = request.POST.get('colecao')
        estado = request.POST.get('estado')
        preco = request.POST.get('preco')
        vend = request.user.username
        trade = request.POST.get('pref1')


        c = Carta_troca(pokemon_name, raridade, colecao, estado, filename, preco, vend, trade)
        c.save()

        return render(request, 'pokecom/troca_form.html')
    return render(request, 'pokecom/troca_form.html')
def criar_torneios(request):
    try:
        organizador = Organizador.objects.get(user=request.user)
        if request.method == 'POST':
            nome_torneio = request.POST.get('nome')
            pais = request.POST.get('pais')
            loja = request.POST.get('loja')
            nome_organizador = organizador.nome_org
            data = request.POST.get('data')
            premio = request.POST.get('premio')

            t = Torneio(nome_torneio = nome_torneio, pais = pais, loja = loja, nome_organizador = nome_organizador,
                data = data, premio = premio)
            t.save()

            return render(request, 'pokecom/criar_torneios.html')
        return render(request, 'pokecom/criar_torneios.html')

    except Organizador.DoesNotExist:
        return HttpResponse("You need a special permition to create tournaments or you have to authenticate as a company")

def torneios(request):
    torneios = Torneio.objects.all()
    p = request.user.username

    if request.method == 'POST':
        torneio_ids = request.POST.get('torneio')
        torneio_sel = Torneio.objects.get(id=torneio_ids)
        if p not in torneio_sel.part.split(','):
            torneio_sel.num_part += 1
            torneio_sel.part += str(p) + str(',')
            torneio_sel.save()
            return redirect('/home')
        return HttpResponse('Já se inscreveu neste torneio')

    return render(request, 'pokecom/torneios.html', {"torneios":torneios})

def procurar(request):
    cartas_disp = Carta.objects.all()

    if request.method == 'POST':
        pesquisado = request.POST['procurar']
        poke_sel = Carta.objects.filter(pokemon__contains=pesquisado)
        return render(request, 'pokecom/comprar.html', {'pesquisado':pesquisado, 'poke_sel':poke_sel})
    else:
        return render(request, 'pokecom/comprar.html', {'cartas_disp':cartas_disp})

def conf_compra(request):
    if request.method == 'POST':
        poke_id = request.POST.get('opcao')
        if poke_id is not None:
            poke_sel = Carta.objects.get(id=poke_id)
            poke_sel.delete()
            return render(request, 'pokecom/conf_compra.html')

        else:
            poke_id = request.POST.get('opcao_p')
            poke_sel = Carta.objects.get(id=poke_id)
            poke_sel.delete()
            return render(request, 'pokecom/conf_compra.html')

    return render(request, 'pokecom/comprar.html')

def procurar_troca(request):
    cartas_disp = Carta_troca.objects.all()

    if request.method == 'POST':
        pesquisado = request.POST['procurar']
        poke_sel = Carta_troca.objects.filter(pokemon__contains=pesquisado)
        return render(request, 'pokecom/trocar.html', {'pesquisado':pesquisado, 'poke_sel':poke_sel})
    else:
        return render(request, 'pokecom/trocar.html', {'cartas_disp':cartas_disp})

def conf_troca(request):
    trader = request.user.username
    if request.method == 'POST':
        poke_id = request.POST.get('opcao')

        if poke_id is not None:
            poke_sel = Carta_troca.objects.get(id=poke_id)
            poke_ideal_sel = poke_sel.trade
            troca_ideal = Carta_troca.objects.filter(Q(vendedor=trader) & Q(pokemon=poke_ideal_sel))
            if troca_ideal.exists() and poke_sel.vendedor != trader:
                poke_sel.delete()
                troca_ideal.delete()
                return render(request, 'pokecom/conf_troca.html')
            return HttpResponse('A troca não pode ser efetuada automáticamente')

        else:
            poke_id = request.POST.get('opcao_p')
            poke_sel = Carta_troca.objects.get(id=poke_id)
            poke_ideal_sel = poke_sel.trade
            troca_ideal = Carta_troca.objects.filter(Q(vendedor=trader) & Q(pokemon=poke_ideal_sel))
            if troca_ideal.exists() and poke_sel.vendedor != trader:
                poke_sel.delete()
                troca_ideal.delete()
                return render(request, 'pokecom/conf_troca.html')
            return HttpResponse('A troca não pode ser efetuada automáticamente')

    return render(request, 'pokecom/trocar.html')