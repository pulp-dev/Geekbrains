import json
import requests

SAVE_PATH = 'repos.json'
TOKEN = 'fdlksfj'


class GitHubUser:
    def __init__(self, token, user_name):
        self.token = token
        self.user_name = user_name

    # получить репозитории пользователя (вся информация о них)
    def get_repos(self):
        r = requests.get('https://api.github.com/user/repos', auth=(self.user_name, self.token))
        return r.json()

    # получить список названий репозиториев
    @staticmethod
    def get_names(r):
        names = []
        for i in r:
            names.append(i['name'])
        return names


def pipeline(save_path, user_name):

    user = GitHubUser(TOKEN, user_name)
    r = user.get_repos()
    names = user.get_names(r)
    with open(save_path, 'w') as f:
        json.dump(names, f, indent=2)


if __name__ == '__main__':
    pipeline(SAVE_PATH, input())
