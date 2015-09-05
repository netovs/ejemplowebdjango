from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre      = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=256)
    receta      = models.IntegerField(default=0)
    pub_date    = models.DateTimeField('Fecha de publicacion')

class Temas(models.Model):
    catid           = models.ForeignKey(Categoria)
    titulo_tema     = models.CharField(max_length=200)
    nombre_imagen   = models.CharField(max_length=200)
    contenido_tema  = models.TextField(max_length=1024)
    menu            = models.IntegerField(default=0)
    activo          = models.IntegerField(default=0)
    

