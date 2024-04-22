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