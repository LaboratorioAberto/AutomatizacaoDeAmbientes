from django.shortcuts import render
from .models import Ambiente

# Create your views here.


def listar_ambientes(request):
    return render(request, 'ambientes/ambientes.html', {'ambientes': Ambiente.objects.all()})

def listar_ambientes_comum(request):
    return render(request, 'ambientes/ambientes-comum.html')
