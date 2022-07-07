from typing import Sequence
from django.contrib import admin

from .models import Tareas

# Register your models here.

class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('nomTarea', 'clave')
    

    
admin.site.register(Tareas, AdministartModelo)