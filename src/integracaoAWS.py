import json
import boto3

def obterDadosBucket(nome_bucket,nome_arquivo):
    # Crie uma instância do cliente S3
    s3 = boto3.client('s3')

    try:
        # Faça a requisição para obter o arquivo do bucket
        response = s3.get_object(Bucket=nome_bucket, Key=nome_arquivo)

        # Leia o conteúdo do arquivo
        file_content = response['Body'].read()
        
        dadosBucket = json.loads(file_content)

        # Faça algo com o conteúdo do arquivo
        return (dadosBucket)

    except Exception as e:
        # Trate qualquer erro que possa ocorrer
        print(f"Erro ao buscar o arquivo: {e}")
        return None