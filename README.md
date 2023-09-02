# Projeto para a Recepção de uma Clínica Veterinária

Com as instruções feitas neste tutorial, será possível ter uma cópia deste projeto em uma máquina local para fins de desenvolvimento, teste e uso.


## Requisitos

Os requisitos básicos para a implementação são o PostgreSQL, na versão 14.9 de preferência, uma IDE para Python (VSCode, PyCharm ou qualquer outra que desejar), a própria linguagem Python instalada, o git Bash em alguma versão (sugere-se a mais recente possível) e, por um breve momento, conexão com Internet.


## Implementação

Para implementar em uma máquina, será necessário inicialmente, realizar a clonagem do repositório para uma pasta, para isso, use o comando abaixo na tela do git-Bash aberto na pasta desejada:

```ps1
git clone https://github.com/guima11/desafio_workshop_backend_2023_2.git
```

Após clonar o repositório, far-se-á necessário a preparação do ambiente virtual (venv) e a instalação das requisições via o arquivo requirements.txt. Para isso, os comandos abaixo no terminal da IDE são necessários nesta ordem:

1. Criar o Ambiente Virtual:

```ps1
python -m venv venv
```

2. Ativar o Ambiente Virtual:

```ps1 
.\venv\Scripts\activate.ps1
```


3. Importar todas as bibliotecas necessárias para o uso da API:

```ps1
pip install -r requirements.txt
```

Seguindo tal passo-a-passo, tem-se o básico para que o servidor possa incializar seguindo a sequência de comandos:

1. Realizar a observação de quaisquer mudanças de código, por precaução (normalmente não será necessário):

```ps1
python manage.py makemigrations
```

2. Migrar os dados para o localhost e preparar o servidor para o funcionamento:

```ps1
python manage.py migrate
```

3. Liberar o servidor para funcionar em máquina local:

```ps1
python manage.py runserver
```

Com isso, se tudo for realizado corretamente, será gerado um link, que ao ser apertado com o mouse junto com a tecla 'Ctrl', abrirá uma página no navegador e o acesso à API será feito.


## Uso 

- Uso da API:

Para um melhor uso da API, deve-se focar no cadastro primeiro do tutor do pet, na URL: /cadastro/tutor/, para depois fazer o do próprio pet na URL: /cadastro/cadastro/, visto que a vinculação do tutor será feita automaticamente. Sugere-se que o usuário tenha uma câmera/webcam para fotografar o pet para identificação posterior, mas o código aceita o cadastro sem foto caso não seja viável.

- Uso no Banco de Dados:

Para a manipulação no banco de dados, sugere-se o uso da ferramenta pg Admin 4, nela o DBA conseguirá realizar todas as manipulações necessárias dos dados conforme o necessário ao acessar o database 'clinicavet' e manipulação das tabelas 'recepvet_cadastro' e 'recepvet_tutor'.


## Sugestões

Sugere-se que o administrador dos dados ou faça a criação de um super usuário com este comando para se cadastrar:

```ps1
py manage.py createsuperuser
```

E usando o /admin após o localhost, terá acesso total a todos os usuários e poderá administrá-los de melhor forma.