import main
    
def test_obterDadosBucket():
    resultado = main.obterDadosBucket('meu-primeiro-bucket', 'resultado.json')
    
    assert resultado == {'nome': 'Joao', 'idade': 25}

def test_obterDadosBucket_erro():
    resultado = main.obterDadosBucket('meu-primeiro-bucket', 'resultado2.json')
    
    assert resultado == 'Erro ao buscar o arquivo: resultado2.json'
