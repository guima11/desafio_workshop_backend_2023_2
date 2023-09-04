from rest_framework import serializers
from .models import Tutor, Cadastro

# Neste arquivo haverá a conversão dos modelos e sua serialização para JSON

# Serialização dos dados de Tutor
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'
        
# Serialização  dos dados de Cadastro        
class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = '__all__'