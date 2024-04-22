# Desenvolvendo para AWS usando Localstack

## Agenda

1. [O que é o Localstack](#o-que-é-o-localstack)
1. [Por que desenvolver localmente](#por-que-desenvolver-localmente)
1. [Como instalar o localstack](#como-instalar)
    1. [Docker Compose](#docker-compose)
    1. [Python](#)
    1. Localstack Desktop

1. [Instalar e configurar a AWS CLI](#instalar-e-configurar-a-aws-cli)
1. [Exemplo completo](#exemplo-de-programa-acessando-local-stack)



## O que é o Localstack

## Por que desenvolver localmente

## [Como instalar](#como-instalar)

### Docker Compose

#### O que é o Docker Compose
Docker Compose é uma ferramenta que permite definir e gerenciar aplicativos multi-container usando arquivos YAML. Com ele, você pode especificar os serviços, redes e volumes necessários para sua aplicação e, em seguida, iniciar todos esses componentes com um único comando.

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


### Instalar e Configurar a AWS CLI

Após a instalação e configuração do Localstack, nosso próximo passo será a instalação e configuração da AWS CLI, para podermos interagir via console com o Localstack e criar os serviços AWS.

Se você tiver instalado o Python e o PIP e preferir instalar via PIP, basta executar o comando no terminal:

```bash
pip install awscli
```

Ou como alternativa, instalar o executável a partir do [site oficial](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#aws-cli) da AWS CLI (minha preferência).

Após a instalação da AWS CLI, vamos configurá-la para ser possível interagir com o Localstack

Crie o arquivo __~/.aws/config__

```ini
[profile localstack]
region=us-east-1
output=json
endpoint_url = http://localhost:4566
```

E posteriormente o arquivo __~/.aws/credentials__
 
```ini
[localstack]
aws_access_key_id=test
aws_secret_access_key=test
```

Nesse momento já é possivel acessar o Localstack usando  a AWS CLI. 
Vamos fazer nosso primeiro teste, criando um bucket S3:

```bash
aws s3 mb s3://meu-primeiro-bucket --profile localstack
```

E posteriormente poderemos consultar se o arquivo S3 foi criado
```bash
aws s3 ls --profile localstack
```

Caso não tenha vários profiles configurados na máquina, pode criar uma variável de ambiente no seu sistema operacional

Windows:
```powershell
set AWS_PROFILE=localstack
```

Linux ou Mac:

```bash
export AWS_PROFILE=localstack
```

Dessa forma, poderá suprimir o comando --profile localstack

```bash
aws s3 ls 
```


## Exemplo de programa acessando Local Stack

Vamos criar um exemplo bem simples usando python, onde vamos acessar um arquivo .json previamente incluído num bucket S3, desserializá-lo e imprimir o conteúdo no console.

Primeiro vamos criar o arquivo resultado.json:

```json
{
    "nome": "Joao",
    "idade": 25
}
```

E depois vamos fazer o upload do arquivo:

```bash
aws s3 cp resultado.json s3://meu-primeiro-bucket/resultado.json
```

```python
import json
import boto3

# Crie uma instância do cliente S3
s3 = boto3.client('s3')

# Nome do bucket S3
bucket_name = 'meu-primeiro-bucket'

# Nome do arquivo a ser buscado
file_name = 'resultado.json'

try:
    # Faça a requisição para obter o arquivo do bucket
    response = s3.get_object(Bucket=bucket_name, Key=file_name)

    # Leia o conteúdo do arquivo
    file_content = response['Body'].read()
       
    cliente = json.loads(file_content)

    # Faça algo com o conteúdo do arquivo
    print(cliente)

except Exception as e:
    # Trate qualquer erro que possa ocorrer
    print(f"Erro ao buscar o arquivo: {e}")
```

Ao executar o programa em python:
```bash
python main.py

```
O resultado esperado (o arquivo resultado.json desserealizado):
```bash
{'nome': 'Joao', 'idade': 25}
```