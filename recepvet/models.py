from django.db import models


# Create your models here.

# Função para carregar a imagem do animal para utilizar no cadastro
def upload_imagem_animal(instance, filename):
    return f"{instance.animal_nome}-{filename}"

# cadastro de Veterinário da clínica
class Vet(models.Model):
    nome = models.CharField(max_length=200, help_text= "Nome do Veterinário")
    choices_gen = [
         ('cao', 'Cão'),
         ('gato', 'Gato'),
         ('ave',  'Ave'),
         ('peixe', 'Peixe'),
         ('exotico', 'Exótico'),
    ]

    expert = models.CharField(choices = choices_gen, max_length=7, verbose_name='Expecialidade')

    def __str__(self):
        return f'Nome: {self.nome}. Expecialidade: {self.expert}.'

    



# Classe de cadastro de Tutor para clínica
class Tutor(models.Model):
    nome = models.CharField(max_length=200, help_text= "Nome do Tutor")
    cpf = models.CharField(help_text = "Digite apenas os dígitos do CPF", verbose_name = "CPF", max_length=11)

   
    def __str__(self):
        return f'Nome: {self.nome}. CPF: {self.cpf}.'

# Classe de Cadastro de pet para clínica
class Cadastro(models.Model):
    animal_nome = models.CharField(max_length = 40, verbose_name='Nome do Animal')

    choices_sexo = [
        ('macho', 'Macho'),
        ('femea',  'Fêmea'),
    ]
    
    status_sexo = models.CharField(choices=choices_sexo, max_length=5, verbose_name='Sexo')

    choices_gen = [
         ('cao', 'Cão'),
         ('gato', 'Gato'),
         ('ave',  'Ave'),
         ('peixe', 'Peixe'),
         ('exotico', 'Exótico'),
    ]

    status_gen = models.CharField(choices = choices_gen, max_length=7, verbose_name='Classificação')

    especie = models.CharField(max_length=100, help_text= 'Caso seja cão ou gato, ponha a raça, se não, a espécie.', verbose_name= 'Raça/Espécie')

    peso = models.FloatField(help_text = 'Peso do animal em kg')

    foto = models.ImageField(upload_to=upload_imagem_animal, blank = True, null = True) # Importação de imagem do animal para animal (blank=True faz com que seja aceito sem a foto)

    sintoma = models.CharField(max_length=1000, verbose_name='Sintomas')

    status_c = [
        ('consulta', 'Consulta'),
        ('retorno', 'Retorno'),
    ]

    tipo_c = models.CharField(choices = status_c, max_length=8, verbose_name='Consulta ou Retorno')

    tutor = models.ForeignKey(
        Tutor,
        max_length=200,
        on_delete=models.CASCADE)
    vet = models.ForeignKey(
        Vet,
        max_length=200,
        on_delete=models.CASCADE)

    