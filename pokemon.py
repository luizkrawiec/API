import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"

while url != None:
    payload = {}
    headers = {}
    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
    url = response['next']

    for item in response['results']:
        print(item['name'])
