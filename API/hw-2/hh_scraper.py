from bs4 import BeautifulSoup as bs
import requests

import time
import json


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 '
}
info_to_search = {
    'name': {'target': '_blank'},
    'salary': {'data-qa': "vacancy-serp__vacancy-compensation"},
    'url': {'class': 'bloko-link'}
}


class HHScraper:
    def __init__(self, headers, vacancy):
        self.headers = headers
        # преобразуем вакансию заменой пробелов на плюсы
        edited_vacancy = '+'.join(vacancy.split())
        # подставляем в url
        self.url = f'https://kirov.hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field' \
                   f'=description&text={edited_vacancy}&from=suggest_post '
        self.params = {'page': 1}
        self.info = {}

    def request(self):
        try:
            r = requests.get(self.url, headers=self.headers, params=self.params)
            r.raise_for_status()
        except Exception as e:
            time.sleep(3)
            self.request()
        return r

    @staticmethod
    def extract_text(element, key):
        return element.find(attrs=info_to_search[key]).text

    def extract_info(self, vacancies):
        for element in vacancies:
            name = self.extract_text(element, 'name')
            while name in self.info.keys():
                name += ' '

            try:
                salary = self.extract_text(element, 'salary')
                while '\u202f' in salary:
                    salary = salary.replace('\u202f', '')
            except AttributeError:
                salary = 'Не указано'

            url = str(element.find(attrs=info_to_search['url'])).split()[3][6:-1]
            self.info[name] = [salary, url, 'hh.ru']

    def next_page(self):
        soup = bs(self.request().content, 'html.parser')
        if len(soup.find_all('a', attrs={'class': 'bloko-button'}, text='дальше')) == 0:
            return
        self.params['page'] += 1
        self.pipeline()

    def pipeline(self):
        soup = bs(self.request().content, 'html.parser')
        vacancies = soup.find_all('div', attrs={'class': 'vacancy-serp-item-body__main-info'})
        self.extract_info(vacancies)
        self.next_page()

    def save_info(self):
        with open('save.json', 'w', encoding='utf-8') as f:
            json.dump(self.info, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    search_request = input()
    scraper = HHScraper(HEADERS, search_request)
    scraper.pipeline()
    scraper.save_info()

