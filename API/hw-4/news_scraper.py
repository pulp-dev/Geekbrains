import requests
from lxml.html import fromstring

import pymongo

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 '
}
mongo_params = {
    'uri': 'mongodb://localhost:27017',
    'database': 'news_scraper',
    'collection': 'news'
}
lenta_url = 'https://lenta.ru/'
yandex_url = 'https://yandex.ru/news/'


class Scraper:
    def __init__(self, headers, url):
        self.headers = headers
        self.url = url

    def make_request(self, url):
        r = requests.get(url, self.headers)
        return r

    def get_date_from_page(self, url, date_lxml):
        r = self.make_request(url)
        dom = fromstring(r.text)
        date = dom.xpath(date_lxml)
        return date

    @staticmethod
    def insert_doc(doc):
        mongo = MongoDBConnector(mongo_params['uri'], mongo_params['database'], mongo_params['collection'])
        mongo.insert_doc(doc)


# для работы с бд
class MongoDBConnector:
    def __init__(self, uri, db, collection):
        self.uri = uri
        self.db = db
        self.collection = collection

    def insert_doc(self, doc):
        with pymongo.MongoClient(self.uri) as client:
            db = client[self.db]
            collection = db[self.collection]
            collection.insert_one(doc)

    def clear_collection(self):
        with pymongo.MongoClient(self.uri) as client:
            db = client[self.db]
            collection = db[self.collection]
            collection.delete_many({})


# для сайта lenta.ru
class LentaScraper(Scraper):
    def __init__(self, headers, url):
        self.headers = headers
        self.url = url
        self.news_lxml = "//a[contains(@class, 'card-mini')]"
        self.title_lxml = ".//*[contains(@class, 'card-mini__title')]/text()"
        self.date_lxml = ".//*[contains(@class, 'card-mini__date')]"

    def extract_info_into_doc(self, element):
        title = element.xpath(self.title_lxml)
        href = 'https://lenta.ru' + element.values()[1]
        try:
            date = element.xpath(self.date_lxml)[0].text
        except IndexError as e:
            date = self.get_date_from_page(href, "//time[@class='topic-header__item topic-header__time']")[0].text

        doc = {
            'Title': title[0],
            'URL': href,
            'Date': date,
            'Source': 'lenta.ru'
        }

        return doc

    def pipeline(self):
        r = self.make_request(self.url)
        dom = fromstring(r.text)
        news_containers = dom.xpath(self.news_lxml)

        for el in news_containers:
            doc = self.extract_info_into_doc(el)
            self.insert_doc(doc)


class YandexNewsScraper(Scraper):
    def __init__(self, headers, url):
        self.headers = headers
        self.url = url
        self.news_lxml = "//*[contains(@class, 'mg-card_flexible')]"
        self.title_lxml = './/h2[@class="mg-card__title"]//text()'
        self.href_lxml = './/a[@class="mg-card__link"]'
        self.date_lxml = ".//span[@class='mg-card-source__time']"
        self.source_lxml = ".//span[@class='mg-card-source__source']//text()"

    def extract_info_into_doc(self, element):
        title = element.xpath(self.title_lxml)[0]
        href = element.xpath(self.href_lxml)[0].values()[0]
        date = element.xpath(self.date_lxml)[0].text
        source = element.xpath(self.source_lxml)[0]

        doc = {
            'Title': title,
            'URL': href,
            'Date': date,
            'Source': source
        }

        return doc

    def pipeline(self):
        r = self.make_request(self.url)
        dom = fromstring(r.text)
        news = dom.xpath(self.news_lxml)
        for el in news:
            doc = self.extract_info_into_doc(el)
            self.insert_doc(doc)


scraper = LentaScraper(HEADERS, lenta_url)
scraper.pipeline()

scraper = YandexNewsScraper(HEADERS, yandex_url)
scraper.pipeline()

# mongo = MongoDBConnector(mongo_params['uri'], mongo_params['database'], mongo_params['collection'])
# mongo.clear_collection()
