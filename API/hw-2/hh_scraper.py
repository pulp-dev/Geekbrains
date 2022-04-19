from bs4 import BeautifulSoup as bs
import time
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 '
}
info_to_search = {
    'name': {'target': '_blank'},
    'salary': {'data-qa': "vacancy-serp__vacancy-compensation"}
}


class HHScraper:
    def __init__(self, headers, vacancy):
        self.headers = headers
        # преобразуем вакансию заменой пробелов на плюсы
        edited_vacancy = '+'.join(vacancy.split())
        # подставляем в url
        self.url = f'https://kirov.hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field' \
                   f'=description&text={edited_vacancy}&from=suggest_post '
        self.vacancies_list = []

    def get_vacancy_block(self, r):
        soup = bs(r.content, 'html.parser')
        vacancies = soup.find_all('div', attrs={'class': 'vacancy-serp-item-body__main-info'})
        return vacancies


scraper = HHScraper(HEADERS, 'python junior')
r = requests.get(scraper.url, headers=scraper.headers)

vacancies = scraper.get_vacancy_block(r)
names = []
for i in vacancies:
    names.append(i.find(attrs=info_to_search['name']).text)
print()
