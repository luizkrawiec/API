import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"

pokemon_list = list()

while url != None:
    payload = {}
    headers = {}
    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
    url = response['next']

    for item in response['results']:
        pokemon_name = item['name']
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response_pokemon = json.loads(requests.request("GET", url_pokemon, headers=headers, data=payload).text)
        
        infos = {
            'name':pokemon_name,
            'id': response_pokemon['id'],
            'height':response_pokemon['height'],
            'weight': response_pokemon['weight'],
            'is_default': response_pokemon['is_default']
        }

        pokemon_list.append(infos)
        print(response_pokemon['id'])

print(pokemon_list)

file_path = r'C:\Users\Luiz Krawiec\OneDrive\Documentos\API\pokemon_files\pokemon_list.json'

with open(file_path, 'w') as outfile:
    print(f'salvando arquivo em:{file_path}')
    json.dump(pokemon_list, outfile)
outfile.close()    