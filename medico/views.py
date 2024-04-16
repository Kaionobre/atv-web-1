
# Create your views here.
from django.shortcuts import render
from .models import Medico

# views.py

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/lista-medicos.html', {'medicos': medicos})

def medico_detalhe(request, pk):
    medico = Medico.objects.get(pk=pk)
    return render(request, 'medico/detalhe-medicos.html', {'medico': medico})



