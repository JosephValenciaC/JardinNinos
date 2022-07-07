from django.shortcuts import render
from .models import Tareas

def pendientes(request):
    tareas = Tareas.objects.all()
    return render(request, 'registros/pendientes.html', {'tareas': tareas})