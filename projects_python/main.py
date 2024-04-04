import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'токен_тренера'
HEADERS = {'trainer_token' : TOKEN, 'Content-Type' : 'application/json' }


body = {
    "name": "Миша",
    "photo": "https://dolnikov.ru/pokemons/albums/765.png"
}


body_change = {
    "pokemon_id": "16374",
    "name": "Тог",
    "photo": "https://dolnikov.ru/pokemons/albums/090.png"
}

body_add = {
    "pokemon_id": "16373"
}


response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)


print(response.text)


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_change)

print(response_change.text)


response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_add)

print(response_add.text)