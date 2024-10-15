from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    matricula = models.CharField(max_length=20, unique=True)
    data_matricula = models.DateField()