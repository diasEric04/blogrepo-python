# cria um projeto 
## `django-admin startproject project .`

# ==========================

# cria um app

## `python manage.py startapp` *nome_do_app*

# ===========================

# starta o servidor do django

## `python manage.py runserver`

# ===========================

# coleta todos os staticfiles e une no caminho colocado na variavel
# definida em [settings.py] 

## `python manage.py collectstatic`

# ===========================

# salva/cria as migrações dos models criados

## `python manage.py makemigrations`

# ===========================

# aplica todas as migrations para criar as tabelas no db

## `python manage.py migrate`

# ===========================

# cria um super user, q tem acesso a area adm e aos banco de dados

## `python manage.py createsuperuser`

# ===========================

# muda a senha do super user

## `python manage.py changepassword` *usuario*

# ===========================

# abre o shell interativo do django que carrega as settings e da setup

## `python manage.py shell`