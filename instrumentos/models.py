from django.db import models

# Create your models here.
class Instrumento(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=[("Viento", "Viento"),("Percusión", "Percusión"),("Cuerda", "Cuerda")])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.marca}-{self.fecha_creacion}"