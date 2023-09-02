from rest_framework import serializers
from .models import Tutor, Cadastro

# Neste arquivo haverá a conversão dos modelos e sua serialização para JSON

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'
        
class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = '__all__'