from django.db import models
from django.utils import timezone
from approfile.models import Avatar

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    fecha = models.DateField(default=timezone.now)
    contenido = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="avatar", null=False, blank=False)

    def __str__(self):
        return f"{self.titulo} | {self.autor}"

