import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'токен_тренера'
HEADERS = {'trainer_token' : TOKEN, 'Content-Type' : 'application/json' }


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 'айди_тренера'})
    assert response.status_code == 200