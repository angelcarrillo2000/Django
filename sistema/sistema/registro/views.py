from ast import Return
from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Persona
from .forms import PersonaForm
from .models import*

# Create your views here.
def inicio (request):
    return render(request, 'paginas/inicio.html')

def Departamentos(request):
    return render(request, 'paginas/departamentos.html')
# acceso a las paginas 

def personas(request):
    personas=Persona.objects.all()
  
    return render(request, 'Persona/index.html', {'personas':personas})

def crear(request):
    formulario=PersonaForm(request.POST or  None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('personas')
    return render(request, 'Persona/crear.html', {'formulario':formulario})

def editar(request,id):
    persona=Persona.objects.get(id=id)
    formulario = PersonaForm(request.POST or  None, request.FILES or None, instance=persona)
    return render(request, 'Persona/editar.html', {'formulario':formulario})
    
    
def eliminar(request, id ):
    persona=Persona.objects.get(id=id)
    persona.delete()
    return redirect ('personas' )
