from django.shortcuts import render
from rest_framework import viewsets 
from .models import Tutor, Cadastro
from .serializers import TutorSerializer, CadastroSerializer
# Create your views here.

# Neste arquivo há a importação dos modelos e das serializações para criação das visualizações para a API

# Classe de visualização para o Tutor
class TutorViewset(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


# Classe de visualização para o Cadastro do pet
class CadastroViewset(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    
