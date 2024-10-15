from django.shortcuts import render
from Serializers import AlunoSerializer
from rest_framework import viewsets
from main.models import Aluno
# Create your views here.
class AlunoViewSets(viewsets.ModelViewSet)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer