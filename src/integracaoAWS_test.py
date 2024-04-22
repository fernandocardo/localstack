import integracaoAWS
    
def test_obterDadosBucket():
    resultado = integracaoAWS.obterDadosBucket('meu-primeiro-bucket', 'resultado.json')
    
    assert resultado == {'nome': 'Joao', 'idade': 25}
