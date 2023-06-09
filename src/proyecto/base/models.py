from django.db import models

# Create your models here.
class Banco(models.Model):
    nombre = models.CharField(max_length=255)
    tasa = models.DecimalField(max_digits=7, decimal_places=6)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    rgb = models.CharField(max_length=10, default='default_value')
    # imagen = models.ImageField(upload_to='banco_imagenes/')
    
    def __str__(self):
        return self.nombre