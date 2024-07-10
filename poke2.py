import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"
all_pokemon = []  # Lista para armazenar todos os Pokémon

while url is not None:
    response = json.loads(requests.get(url).text)
    all_pokemon.extend(response['results'])  # Adiciona os novos resultados à lista
    url = response['next']  # Atualiza a URL para a próxima página

for item in all_pokemon:
    print(item['name'])