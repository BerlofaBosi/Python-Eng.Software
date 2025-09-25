import requests

def buscaCEP(cep: str):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    r = requests.get(url)
    infos = r.json()
    return f'Rua: {infos['logradouro']}, \nBairro: {infos['bairro']}, \nCidade: {infos['localidade']}, \nEstado: {infos['estado']}.'

print(buscaCEP('09190430'))
