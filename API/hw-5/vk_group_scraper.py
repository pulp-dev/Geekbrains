import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pymongo import MongoClient

from tqdm import trange

# selenium
DRIVER_PATH = r'../lesson5/geckodriver/geckodriver.exe'
URL = 'https://vk.com/tokyofashion'
MAX_PAGE_NUM = 5

# mongodb
mongo_params = {
    'uri': 'mongodb://localhost:27017',
    'database': 'TokyoFashion',
    'collection': 'posts'
}


class MongoDBConnector:
    def __init__(self, uri, db, collection):
        self.uri = uri
        self.db = db
        self.collection = collection

    def insert_doc(self, doc):
        with MongoClient(self.uri) as client:
            db = client[self.db]
            collection = db[self.collection]
            collection.insert_one(doc)

    def clear_collection(self):
        with MongoClient(self.uri) as client:
            db = client[self.db]
            collection = db[self.collection]
            collection.delete_many({})


class VKScraper(MongoDBConnector):
    def __init__(self, uri, db, collection, url, driver_path):
        # mongo params
        self.uri = uri
        self.db = db
        self.collection = collection

        # selenium params
        self.url = url
        self.driver_path = driver_path

        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--start-maximized")

        self.driver = webdriver.Firefox(executable_path=self.driver_path, options=self.options)

    def scroll(self):
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.END)
        actions.key_up(Keys.END)
        actions.perform()

        self.close_push_window()

        time.sleep(1)
        posts = self.driver.find_elements_by_xpath("//div[@class='_post_content']")
        return posts

    def close_push_window(self):
        try:
            button = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "UnauthActionBox__close")
                )
            )
            button.click()
        except Exception:
            return

    def extract_info_into_doc(self, element):
        date = element.find_elements_by_class_name("post_date")[0].text
        text = element.find_elements_by_class_name("wall_post_text")[0].text
        href = element.find_elements_by_xpath(".//*[@class='post_link']")[0].get_attribute('href')
        likes = element.find_elements_by_xpath(".//*[contains(@class, 'PostBottomAction__count')]")[0].text
        reposts = element.find_elements_by_xpath(".//*[contains(@class, 'PostBottomAction__count')]")[1].text

        if text == "":
            return

        try:
            likes = int(likes)
        except ValueError:
            likes = 0

        try:
            reposts = int(reposts)
        except ValueError:
            reposts = 0

        doc = {
            'Date': date,
            'Post': text,
            'URL': href,
            'Likes': likes,
            'Reposts': reposts
        }
        return doc

    def search(self, request):
        button = self.driver.find_elements_by_xpath("//*[@class='ui_tab_plain ui_tab_search']")
        button[0].click()

        input_field = self.driver.find_element_by_id("wall_search")
        input_field.send_keys(request + Keys.ENTER + Keys.TAB)

    def pipeline(self, request):
        self.driver.get(self.url)
        time.sleep(1)
        self.search(request)
        index = 0
        for i in range(5):
            posts = self.scroll()
            for el in posts[index:]:
                doc = self.extract_info_into_doc(el)
                try:
                    self.insert_doc(doc)
                except:
                    continue
            index = len(posts) - 1


if __name__ == '__main__':
    search_request = input()
    scraper = VKScraper(mongo_params['uri'], mongo_params['database'], mongo_params['collection'], URL, DRIVER_PATH)
    scraper.pipeline(search_request)
