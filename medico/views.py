
# Create your views here.
from django.shortcuts import render
from .models import Medico

# views.py

def medico_nomeado(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/info.html', {'posts': medicos})

def medico_lista(request, pk):
    medico = Medico.objects.get(pk=pk)
    return render(request, 'medico/info.html', {'post': medico})



