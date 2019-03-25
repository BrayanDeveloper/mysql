from django.db import models

# Create your models here.

class Videojuego(models.Model):
	nombre = models.CharField(max_length=20)
	codigo = models.CharField(max_length=20)
	tipo = models.CharField(max_length=20)
	version = models.CharField(max_length=20)
	fecha = models.DateTimeField(auto_now=True)
	
