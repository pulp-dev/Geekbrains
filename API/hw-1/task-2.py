import requests
import json

from random import randint

PATH = 'random_gif.json'
params = {
    'api_key': 'eadMwxGByABL7fhcLimkOZTf4lb2vcOu'
}


# поиск по ключевому слову
def get_all_gifs_related_to_keywrd(key_wrd, params):
    params['q'] = key_wrd
    r = requests.get('https://api.giphy.com/v1/gifs/search', params=params)
    return r.json()


# случайное gif
def pick_random_gif(json):
    length = len(json['data'])
    return json['data'][randint(0, length - 1)]['url']


def pipeline(path):
    result = get_all_gifs_related_to_keywrd(input(), params)
    url = pick_random_gif(result)
    with open(path, 'w')as f:
        json.dump(url, f, indent=2)


if __name__ == '__main__':
    pipeline(PATH)
