import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import undetected_chromedriver as uc
from dotenv import load_dotenv
from notifiers.logging import NotificationHandler
from loguru import logger

from config import TagAvito

load_dotenv()

driver = uc.Chrome()
url =  os.getenv('URL')


class AvitoParse:
    """
    Парсинг авито url - ссылка на авито которую нужно пропарсить
    count_page - количество проверяемых страниц
    items - ключевые слова в иписании
    """
    def __init__(self, url:str, items:list, count_page:int = 50, tg_token: str = None,):
        self.url = url
        self.items = items
        self.count_page = count_page
        self.data = []
        self.tg_token = tg_token


    def start_browser(self):
        options = Options()
        useragent = UserAgent()
        options.add_argument('--headless')
        options.add_argument(f"user-agent={useragent.random}")
        self.driver = uc.Chrome(options=options)


    def get_url(self):
        self.driver.get(self.url)

    def paginations(self):
        logger.info('Страница успешно загружена. Просматриваю объявления')
        while self.count_page > 0:
            self.parse_page()
            if self.driver.find_elements(By.CSS_SELECTOR, "[data-marker*='pagination-button/nextPage']"):
                self.driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']").click()
                self.count_page -= 1
                logger.debug("Следующая страница")
            else:
                logger.info("Нет кнопки дальше")
                break

    def parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[class*='item-descriptionStep']").text
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')
            data = {
                'name': name,
                'description': description,
                'url': url,
                'price': price,
            }
            if any([item.lower() in description.lower() for item in self.items]) and int(price)==0:
                self.data.append(data)
                print(data)
        self.save_data()
    def save_data(self):
        with open("items.json", 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def parse(self):
        self.start_browser()
        self.get_url()
        self.paginations()


if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read("settings.ini")
    token =  os.getenv('TG_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    if token and chat_id:
        params = {
            'token': token,
            'chat_id': chat_id
        }
        tg_handler = NotificationHandler("telegram", defaults=params)
        logger.add(tg_handler, level="SUCCESS", format="{message}")
    try:
        AvitoParse(url=url, count_page=30, items=['монитор', 'чехол']).parse()
    except Exception as error:
        logger.error(error)
    
