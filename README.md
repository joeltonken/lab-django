# Laboratório de Exames

Este é um aplicativo web desenvolvido em Django para gerenciamento de um laboratório de exames. Ele permite o cadastro de pacientes, médicos, exames e resultados de exames.

## Requisitos

- Python
- Django

## Instalação

1. Clone o repositório para o seu ambiente local:

```   
git clone https://github.com/joeltonken/lab-django.git
```
   
2. Acesse o diretório do projeto:
   
```
cd lab-django
```

3. Crie um ambiente virtual e ative-o:
   
```    
python -m venv venv
    
venv/Scripts/Activate
```

4. Instale as dependências do projeto:
   
```
pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:
   
```
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:
   
```
python manage.py runserver
```
  
7. Acesse o aplicativo em seu navegador através do endereço `http://localhost:8000`.