from bs4 import BeautifulSoup as bs
import requests

from pymongo import MongoClient

import time
import json
import re


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 '
}
MONGO = {
    'uri': 'mongodb://localhost:27017',
    'database': 'hh_scraper',
    'collection': 'jobs'
}
info_to_search = {
    'name': {'target': '_blank'},
    'salary': {'data-qa': "vacancy-serp__vacancy-compensation"},
    'url': {'class': 'bloko-link'}
}


class HHScraper:
    def __init__(self, headers, vacancy, mongo_uri, mongo_db, mongo_collection):
        self.headers = headers
        # преобразуем вакансию заменой пробелов на плюсы
        edited_vacancy = '+'.join(vacancy.split())
        # подставляем в url
        self.url = f'https://kirov.hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field' \
                   f'=description&text={edited_vacancy}&from=suggest_post '
        self.params = {'page': 1}
        self.info = {}

        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @staticmethod
    def extract_text(element, key):
        return element.find(attrs=info_to_search[key]).text

    @staticmethod
    def cursor_length(cursor):
        count = 0
        for i in cursor:
            count += 1
        return count

    def push_to_db(self, collection, doc, check_for_individuality=False):
        if check_for_individuality:
            cur = collection.find({
                'URL': doc['URL']
            })
            if self.cursor_length(cur) == 0:
                collection.insert_one(doc)
            else:
                print('Уже есть')
        else:
            collection.insert_one(doc)

    def request(self):
        try:
            r = requests.get(self.url, headers=self.headers, params=self.params)
            r.raise_for_status()
        except Exception as e:
            time.sleep(3)
            self.request()
        return r

    def extract_info(self, vacancies):
        for element in vacancies:
            name = self.extract_text(element, 'name')
            while name in self.info.keys():
                name += ' '

            try:
                string = self.extract_text(element, 'salary')
                salary = int(re.search(r'[ ]+[0-9]+', string).group().strip()) * 1000
            except:
                salary = 0

            url = str(element.find(attrs=info_to_search['url'])).split()[3][6:-1]
            self.info[name] = [salary, url, 'hh.ru']

            with MongoClient(self.mongo_uri) as client:
                db = client[self.mongo_db]
                collection = db[self.mongo_collection]

                doc = {
                    'Title': name,
                    'Salary': salary,
                    'URL': url,
                    'Source': 'hh.ru'
                }

                self.push_to_db(collection, doc, check_for_individuality=True)

    def next_page(self):
        soup = bs(self.request().content, 'html.parser')
        if len(soup.find_all('a', attrs={'class': 'bloko-button'}, text='дальше')) == 0:
            return
        self.params['page'] += 1

    def pipeline(self):
        soup = bs(self.request().content, 'html.parser')
        vacancies = soup.find_all('div', attrs={'class': 'vacancy-serp-item-body__main-info'})
        self.extract_info(vacancies)
        self.next_page()
        self.pipeline()

    def save_info(self):
        with open('save.json', 'w', encoding='utf-8') as f:
            json.dump(self.info, f, indent=2, ensure_ascii=False)

    def search_by_salary(self, down_limit):
        with MongoClient(self.mongo_uri) as client:
            db = client[self.mongo_db]
            collection = db[self.mongo_collection]

            cur = collection.find({
                'Salary': {'$gt': down_limit}
            })
            return list(cur)


if __name__ == '__main__':
    search_request = input()
    scraper = HHScraper(HEADERS, search_request, MONGO['uri'], MONGO['database'], MONGO['collection'])
    scraper.pipeline()
    scraper.save_info()
    result = scraper.search_by_salary(100000)
