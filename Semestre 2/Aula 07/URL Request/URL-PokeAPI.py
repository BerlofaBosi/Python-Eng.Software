import requests

def buscaPokemon(nome: str):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
    r = requests.get(url)
    infos = r.json()
    return f"ID: {infos['id']}, \nTipo: {[i['type']['name'] for i in infos['types']]}."

print(buscaPokemon('pikachu'))
