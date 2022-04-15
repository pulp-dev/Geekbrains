import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv(".env")

client_id = os.environ.get("CLIENT")
client_secret = os.environ.get("SECRET")
params = {
    'client_id': client_id,
    'client_secret': client_secret
}

URL_TEMPLATE = f"https://api.artsy.net/api/tokens/xapp_token?client_id={client_id}&client_secret={client_secret}"


def create_headers(token):
    return {'X-Xapp-Token': token}


def get_tempo_token_info(url, params):
    response = requests.post(URL_TEMPLATE, params=params)
    response.raise_for_status()
    info = response.json()
    return info['token'], info['expires_at']


token, expires_at = get_tempo_token_info(URL_TEMPLATE, params)


