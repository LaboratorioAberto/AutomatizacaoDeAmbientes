from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Embarcado, Rede, Atuador, Sensor

# Create your views here.


def login(request):
    metodo = request.method
    if metodo == "POST":
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                return HttpResponseRedirect('/admin/')
            else:
                if user.has_perm("controle.add_boarded"):
                    return HttpResponseRedirect('/embarcados/')
                else:
                    return HttpResponseRedirect('/embarcados-comum/')
        else:
            return render(request, 'controle/login2.html', {'mensagem': 'Usuário inválido! Tente novamente!',
                                                            'metodo': metodo})
    return render(request, 'controle/login2.html', {'metodo': metodo})


def listar_embarcados(request):
    return render(request, 'controle/embarcados.html', {'embarcados': Embarcado.objects.all()})


def listar_embarcados_comum(request):
    return render(request, 'controle/embarcados-comum.html', {'embarcados': Embarcado.objects.all()})


def add_embarcado(request):
    return render(request, 'controle/adicionar-embarcado.html', {'atuadores': Atuador.objects.all(),
                                                                 'sensores': Sensor.objects.all()})


def listar_ambientes(request):
    return render(request, 'controle/ambientes.html')
