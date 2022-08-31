from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length=6 ,primary_key=True)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        txt = "Asignatura: {0}, Codigo: {1}"
        return txt.format(self.nombre, self.codigo)

