from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo= models.CharField(max_length=100)
    #atajos poner mc y enter y se crea lo de abajo (char)
    subtitulo = models.CharField(max_length=50)
    #atajos poner mi y enter y se crea lo de abajo (entero)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ', ' + self.subtitulo
