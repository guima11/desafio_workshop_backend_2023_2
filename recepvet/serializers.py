from rest_framework import serializers
from .models import Tutor, Cadastro, Vet

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

# Serialização  dos dados do Veterinário    
class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = '__all__'
