from django.db import models

# Create your models here.

class turma(models.Model):
    codigo = models.CharField(max_length=100)
    codigoCurso = models.CharField(max_length=100)
   

    def __str__(self):
        return self.nome