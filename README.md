# Desenvolvendo para AWS usando Localstack

## Agenda

1. [O que é o Localstack](#o-que-é-o-localstack)
1. [Por que desenvolver localmente](#porque-localmente)
1. [Como instalar o localstack](#como-instalar)
    1. Docker Compose
    1. Python
    1. Localstack Desktop
1.


## [O que é o Localstack](#o-que-é-o-localstack)


## [Por que desenvolver localmente](#porque-localmente)


## [Como instalar](#como-instalar)

### Docker Compose

#### O que é o Docker Compose
Docker Compose é uma ferramenta que permite definir e gerenciar aplicativos multi-container usando arquivos YAML. Com ele, você pode especificar os serviços, redes e volumes necessários para sua aplicação e, em seguida, iniciar todos esses componentes com um único comando.

####
A maneira mais fácil e recomendada de obter o Docker Compose é instalando o Docker Desktop. 
O Docker Desktop inclui o Docker Compose, juntamente com o Docker Engine e o Docker CLI, que são pré-requisitos para o Compose.

Certifique-se de ter o Docker Desktop instalado. 
Se já o tiver, você pode verificar a versão do Compose selecionando “About Docker Desktop” no menu do Docker.
O Docker Desktop está disponível para Linux, Mac e Windows.

Criei um arquivo chamado docker-compose.yml com o seguinte conteúdo:

```yaml
version: "3.8"

services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
    environment:
      # LocalStack configuration: https://docs.localstack.cloud/references/configuration/
      - DEBUG=${DEBUG:-0}
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
```

Em seguida, no terminal, rode o docker-compose:

```bash
docker-compose up
```

Nesse momento o localstack já está funcionando, mas para deixar a experiência um pouco mais visual, vamos instalar no Docker Desktop, a extensão do localstack.

Primeiro, abra seu Docker Desktop:

![Docker Desktop](/doc/images/docker-desktop.png "Docker Desktop")

Clique na esquerda em add Extension e busque pela extensão LocalStack.

![Extensão Localstack](/doc/images/extensao-local-stack.png "Extensão Localstack")

Clique em "Install"


Quando seu docker-compose estiver rodando, você verá a extensão dessa forma:

![Extensão Localstack Rodando](/doc/images/extensao-local-stack-rodando.png "Extensão Localstack Rodando")

Você também pode clicar no botão "Local Stack Web Aplication", que vai abrir seu navegador no endereço https://app.localstack.cloud/dashboard .

Busque no menu lateral por "Resorce Browser", para ver o serviços disponíveis no localstack. Posteriormente vamos interagir com eles.