# atenção

## é necessario buildar o container se modificar, os scripts, dockerfile ou 
## docker-compose

# ==========================

# builda o projeto

## `docker-compose up --build`

# ==========================

# sobe o container (sem travar o terminal)

## `docker-compose up -d`

# ==========================

# derruba o container

## `docker-compose down`

# ==========================

# lista os container ativos

## `docker ps -a`

# ==========================

# remove o container pelo id

## `docker rm` *id*

# ==========================

# lista as imagens

## `docker image ls`

# ==========================

# apaga a imagens pelo id

## `docker image rm` *id*
## `docker rmi` *id*

# ==========================

# executa comandos pelo container do app (--rm fecha logo apos)

## `docker-compose run --rm djangoapp` *comando*

### ex
### `docker-compose run --rm djangoapp python -V`

### como o Dockerfile copia a pasta de scripts, os scripts param na raiz do 
### container, ou seja, se eu utilizar o comando posso usar o nome do script
### para executa-lo, ex:

### `docker-compose run --rm djangoapp` [runserver.sh]

# ==========================

# com o container rodando, ele abre o shell do container

## `docker exec -it djangoapp` [/bin/sh] ou [sh]

