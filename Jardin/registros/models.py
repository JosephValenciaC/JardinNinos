from django.db import models


class Tareas(models.Model): #Define la estructura de la tabla
    
    nomTarea = models.CharField(max_length=50, verbose_name="Nombre de la tarea")
    clave = models.CharField(max_length=50, verbose_name="Clave")
    descripcion = models.TextField(verbose_name="Descripcion")
    grado = models.CharField(max_length=50, verbose_name="Grado")
    FechaEntrega = models.CharField(max_length=50 ,verbose_name="Fecha de entrega")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen del Curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True) #Fecha de actualizacion
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["created"]
    def __str__(self):
        return self.nomTarea